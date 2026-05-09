"""
Extract structured questions from IGCSE Physics PDF files (Paper 3/4).

For each non-MCQ PDF in the "June Exam Paper Sample" folder:
  1. Detects question boundaries using bold question numbers on the left margin.
  2. Identifies multi-page questions (continuation pages with no new question number).
  3. Renders each page at high DPI, crops out headers/footers, trims whitespace.
  4. Produces TWO output modes:
     - Option A ("stitched"): All pages of a question stitched into one tall image.
     - Option B ("pages"):    Each page exported separately as Q03_p1.png, Q03_p2.png, etc.
  5. All images have the same width. Dotted answer lines are kept.

Requirements: PyMuPDF (fitz), Pillow, numpy
"""

import fitz  # PyMuPDF
import os
import re
import io
from PIL import Image
import numpy as np

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
DPI = 250                   # Render resolution
SCALE = DPI / 72.0          # PDF coords are 72 DPI
TARGET_WIDTH = 1200          # All exported images will be this width (px)
LEFT_MARGIN_CUTOFF = 93      # PDF x-coord: content starts here (right of Q number)
TOP_HEADER_CUTOFF = 25       # PDF y-coord: skip header area above this
BOTTOM_FOOTER_CUTOFF = 780   # PDF y-coord: skip footer area below this
PADDING_TOP = 12             # Extra pixels of padding above the crop
PADDING_BOTTOM = 10          # Extra pixels of padding below the crop
PADDING_LEFT = 8             # Extra pixels of padding on the left
PADDING_RIGHT = 10           # Extra pixels of padding on the right
STITCH_GAP = 10              # Pixels between stitched page segments

PDF_DIR = r"c:\Users\User\Desktop\Exercises\June Exam Paper Sample"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def find_question_starts(doc):
    """
    Scan all pages to find where each top-level question starts.
    Returns a list of (question_number, start_page_index).
    
    A new question is identified by a bold integer (1-200) appearing at the
    left margin, with font size >= 11.
    """
    question_starts = []

    for page_idx in range(doc.page_count):
        page = doc[page_idx]
        blocks = page.get_text("dict")["blocks"]

        for block in blocks:
            if block["type"] != 0:
                continue
            bbox = block["bbox"]
            # Question numbers are on the left margin
            if bbox[0] > LEFT_MARGIN_CUTOFF:
                continue
            if bbox[1] < TOP_HEADER_CUTOFF:
                continue

            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    text = span["text"].strip()
                    span_bbox = span["bbox"]
                    span_size = span.get("size", 0)
                    span_flags = span.get("flags", 0)

                    if span_bbox[0] > LEFT_MARGIN_CUTOFF:
                        continue
                    if span_bbox[1] < TOP_HEADER_CUTOFF:
                        continue

                    # Must be a standalone integer
                    if not re.match(r'^\d{1,3}$', text):
                        continue
                    num = int(text)
                    if num < 1 or num > 200:
                        continue
                    # Must be reasonably sized (not a tiny label)
                    if span_size < 11:
                        continue

                    question_starts.append((num, page_idx))

    return question_starts


def build_question_page_ranges(doc, question_starts):
    """
    Given the list of (q_num, start_page), determine the page range for
    each question. A question spans from its start page up to (but not
    including) the next question's start page, or the end of the document.
    
    Returns: list of (q_num, [page_indices])
    """
    # Skip the cover/title page (page 0 typically has no question)
    # Deduplicate and sort by page index
    seen = {}
    for q_num, page_idx in question_starts:
        if q_num not in seen or page_idx < seen[q_num]:
            seen[q_num] = page_idx

    sorted_qs = sorted(seen.items(), key=lambda x: x[1])

    ranges = []
    for i, (q_num, start_page) in enumerate(sorted_qs):
        if i + 1 < len(sorted_qs):
            end_page = sorted_qs[i + 1][1]  # exclusive
        else:
            end_page = doc.page_count
        pages = list(range(start_page, end_page))
        ranges.append((q_num, pages))

    return ranges


def render_page_content(page, is_first_page_of_question=True):
    """
    Render a page at high DPI and crop out headers/footers.
    For the first page of a question, also exclude the question number
    from the left margin.
    For continuation pages, include content from the left edge (since
    sub-part labels like (a), (b) may start there).
    
    Returns a PIL Image of the cropped content area, or None if empty.
    """
    pix = page.get_pixmap(dpi=DPI)
    page_img = Image.open(io.BytesIO(pix.tobytes("png")))

    # Ensure RGB
    if page_img.mode == "RGBA":
        bg = Image.new("RGB", page_img.size, (255, 255, 255))
        bg.paste(page_img, mask=page_img.split()[3])
        page_img = bg
    elif page_img.mode != "RGB":
        page_img = page_img.convert("RGB")

    page_rect = page.rect
    img_w, img_h = page_img.size

    # Determine crop boundaries in pixels
    y_top = int(TOP_HEADER_CUTOFF * SCALE)
    y_bottom = min(int(BOTTOM_FOOTER_CUTOFF * SCALE), img_h)

    if is_first_page_of_question:
        x_left = int(LEFT_MARGIN_CUTOFF * SCALE) - PADDING_LEFT
    else:
        # On continuation pages, sub-part labels (a), (b) start further left
        x_left = int(LEFT_MARGIN_CUTOFF * SCALE) - PADDING_LEFT

    x_right = img_w - PADDING_RIGHT

    # Clamp
    x_left = max(0, x_left)
    y_top = max(0, y_top)
    x_right = min(img_w, x_right)
    y_bottom = min(img_h, y_bottom)

    if x_right <= x_left or y_bottom <= y_top:
        return None

    cropped = page_img.crop((x_left, y_top, x_right, y_bottom))

    # Trim whitespace from top and bottom
    arr = np.array(cropped)
    if len(arr.shape) == 3:
        gray = np.mean(arr, axis=2)
    else:
        gray = arr

    row_means = np.mean(gray, axis=1)
    non_white = np.where(row_means < 250)[0]

    if len(non_white) == 0:
        return None  # Blank page

    first_row = max(non_white[0] - PADDING_TOP, 0)
    last_row = min(non_white[-1] + PADDING_BOTTOM + 1, cropped.height)

    if last_row <= first_row:
        return None

    trimmed = cropped.crop((0, first_row, cropped.width, last_row))

    if trimmed.height < 15:
        return None

    return trimmed


def resize_to_target_width(img, target_width=TARGET_WIDTH):
    """Resize image to target width while maintaining aspect ratio."""
    if img.width == 0:
        return img
    ratio = target_width / img.width
    new_height = max(1, int(img.height * ratio))
    return img.resize((target_width, new_height), Image.LANCZOS)


def stitch_images_vertically(images, gap=STITCH_GAP):
    """
    Stitch multiple images vertically into one tall image.
    All images should already have the same width.
    """
    if not images:
        return None
    if len(images) == 1:
        return images[0]

    total_height = sum(img.height for img in images) + gap * (len(images) - 1)
    width = images[0].width

    stitched = Image.new("RGB", (width, total_height), (255, 255, 255))
    y_offset = 0
    for img in images:
        stitched.paste(img, (0, y_offset))
        y_offset += img.height + gap

    return stitched


# ---------------------------------------------------------------------------
# Main extraction logic
# ---------------------------------------------------------------------------

def extract_structured_questions(pdf_path):
    """
    Extract all structured questions from a single PDF.
    Returns list of (q_num, stitched_image, page_images) tuples.
    """
    doc = fitz.open(pdf_path)
    basename = os.path.basename(pdf_path)

    print(f"\n  Processing: {basename}")
    print(f"  Pages: {doc.page_count}")

    # Find where each question starts
    question_starts = find_question_starts(doc)

    if not question_starts:
        print(f"  No questions found in {basename}")
        doc.close()
        return []

    # Build page ranges for each question
    q_ranges = build_question_page_ranges(doc, question_starts)
    print(f"  Found {len(q_ranges)} questions")

    results = []

    for q_num, pages in q_ranges:
        page_images = []
        for i, page_idx in enumerate(pages):
            page = doc[page_idx]
            is_first = (i == 0)
            page_content = render_page_content(page, is_first_page_of_question=is_first)
            if page_content is not None:
                # Resize to target width
                page_content = resize_to_target_width(page_content)
                page_images.append(page_content)

        if not page_images:
            print(f"    WARNING: Q{q_num} produced no images, skipping")
            continue

        # Stitch all pages together (Option A)
        stitched = stitch_images_vertically(page_images)

        results.append((q_num, stitched, page_images))
        pages_str = f" ({len(page_images)} pages)" if len(page_images) > 1 else ""
        print(f"    Q{q_num}: {len(pages)} PDF pages -> {len(page_images)} image(s){pages_str}")

    doc.close()
    return results


def process_all_structured_pdfs(pdf_dir):
    """Process all structured question PDFs (non-MCQ) in the directory."""
    pdf_files = sorted([
        f for f in os.listdir(pdf_dir)
        if f.lower().endswith(".pdf") and "mcq" not in f.lower()
    ])

    if not pdf_files:
        print("No structured question PDFs found in:", pdf_dir)
        return

    print(f"Found {len(pdf_files)} structured question PDFs.")

    for pdf_file in pdf_files:
        pdf_path = os.path.join(pdf_dir, pdf_file)
        base_name = os.path.splitext(pdf_file)[0]

        # Create output folders
        stitched_dir = os.path.join(pdf_dir, base_name, "stitched")
        pages_dir = os.path.join(pdf_dir, base_name, "pages")
        os.makedirs(stitched_dir, exist_ok=True)
        os.makedirs(pages_dir, exist_ok=True)

        # Extract questions
        results = extract_structured_questions(pdf_path)

        if not results:
            print(f"  No questions extracted from {pdf_file}")
            continue

        stitched_count = 0
        page_count = 0

        for q_num, stitched_img, page_images in results:
            # Option A: Save stitched image
            stitched_path = os.path.join(stitched_dir, f"Q{q_num:02d}.png")
            stitched_img.save(stitched_path, "PNG", optimize=True)
            stitched_count += 1

            # Option B: Save individual page images
            if len(page_images) == 1:
                page_path = os.path.join(pages_dir, f"Q{q_num:02d}.png")
                page_images[0].save(page_path, "PNG", optimize=True)
                page_count += 1
            else:
                for p_idx, p_img in enumerate(page_images):
                    page_path = os.path.join(pages_dir, f"Q{q_num:02d}_p{p_idx + 1}.png")
                    p_img.save(page_path, "PNG", optimize=True)
                    page_count += 1

        print(f"  Option A: {stitched_count} stitched images -> {stitched_dir}")
        print(f"  Option B: {page_count} page images -> {pages_dir}")

    print("\nDone!")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    process_all_structured_pdfs(PDF_DIR)
