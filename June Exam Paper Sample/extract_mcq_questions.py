"""
Extract individual MCQ questions from IGCSE Physics PDF files.

For each PDF in the "June Exam Paper Sample" folder:
  1. Renders each page at high DPI.
  2. Detects question boundaries using the bold question numbers on the left margin.
  3. Crops each question EXCLUDING the question number.
  4. Exports all images with the same width.
  5. Saves images into a subfolder named after the PDF (without extension).

Requirements: PyMuPDF (fitz), Pillow
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
DPI = 250                  # Render resolution (higher = sharper images)
SCALE = DPI / 72.0         # PDF coords are 72 DPI
TARGET_WIDTH = 1200         # All exported images will be this width (px)
LEFT_MARGIN_CUTOFF = 93     # PDF x-coord: content starts here (to the right of the Q number)
TOP_HEADER_CUTOFF = 30      # PDF y-coord: skip header area above this
BOTTOM_FOOTER_CUTOFF = 770  # PDF y-coord: skip footer area below this
PADDING_TOP = 12            # Extra pixels of padding above the crop
PADDING_BOTTOM = 10         # Extra pixels of padding below the crop
PADDING_LEFT = 8            # Extra pixels of padding on the left
PADDING_RIGHT = 10          # Extra pixels of padding on the right

PDF_DIR = r"c:\Users\User\Desktop\Exercises\June Exam Paper Sample"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def is_question_number(text, font_flags):
    """
    Check if a text span is a standalone question number.
    Question numbers are typically bold integers (1-99) at the left margin.
    font_flags: bit 0 = superscript, bit 1 = italic, bit 2 = serif, bit 4 = bold
    """
    text = text.strip()
    if not text:
        return False
    # Must be a pure integer
    if not re.match(r'^\d{1,3}$', text):
        return False
    num = int(text)
    return 1 <= num <= 200


def find_question_positions(page):
    """
    Find the (question_number, y_position) for each question on a page.
    Returns a sorted list of (q_num, y_top) tuples.
    """
    questions = []
    blocks = page.get_text("dict")["blocks"]

    for block in blocks:
        if block["type"] != 0:  # text block only
            continue

        bbox = block["bbox"]
        # Question numbers appear on the left margin (x < LEFT_MARGIN_CUTOFF)
        # and below the header
        if bbox[0] > LEFT_MARGIN_CUTOFF:
            continue
        if bbox[1] < TOP_HEADER_CUTOFF:
            continue

        for line in block.get("lines", []):
            for span in line.get("spans", []):
                span_text = span["text"].strip()
                span_bbox = span["bbox"]
                span_flags = span.get("flags", 0)

                # Check if this span sits in the left margin area
                if span_bbox[0] > LEFT_MARGIN_CUTOFF:
                    continue
                if span_bbox[1] < TOP_HEADER_CUTOFF:
                    continue

                if is_question_number(span_text, span_flags):
                    q_num = int(span_text)
                    y_top = span_bbox[1]  # top y of the question number
                    questions.append((q_num, y_top))

    # Sort by y position (top to bottom)
    questions.sort(key=lambda x: x[1])
    return questions


def find_content_bottom(page, q_y_top, next_q_y_top, page_height):
    """
    Find the bottom boundary of a question's content.
    This is either:
      - Just above the next question number, or
      - The bottom of the page content area.
    We also trim whitespace from the bottom.
    """
    if next_q_y_top is not None:
        # Stop just before the next question (with a small gap)
        return next_q_y_top - 5
    else:
        return min(BOTTOM_FOOTER_CUTOFF, page_height)


def trim_whitespace_bottom(img_array, bg_threshold=250):
    """
    Trim empty whitespace rows from the bottom of a grayscale/RGB image array.
    Returns the index of the last non-white row + some padding.
    """
    if len(img_array.shape) == 3:
        # Convert to grayscale for analysis
        gray = np.mean(img_array, axis=2)
    else:
        gray = img_array

    # Find rows that are NOT all white
    row_means = np.mean(gray, axis=1)
    non_white_rows = np.where(row_means < bg_threshold)[0]

    if len(non_white_rows) == 0:
        return img_array.shape[0]  # All white, return full height

    last_content_row = non_white_rows[-1]
    return min(last_content_row + PADDING_BOTTOM + 1, img_array.shape[0])


def trim_whitespace_top(img_array, bg_threshold=250):
    """
    Trim empty whitespace rows from the top of a grayscale/RGB image array.
    Returns the index of the first non-white row.
    """
    if len(img_array.shape) == 3:
        gray = np.mean(img_array, axis=2)
    else:
        gray = img_array

    row_means = np.mean(gray, axis=1)
    non_white_rows = np.where(row_means < bg_threshold)[0]

    if len(non_white_rows) == 0:
        return 0

    first_content_row = non_white_rows[0]
    return max(first_content_row - PADDING_TOP, 0)


def crop_question(page_img, q_y_top, content_bottom, page_rect):
    """
    Crop a single question from the rendered page image.
    Excludes the question number by starting from LEFT_MARGIN_CUTOFF.
    """
    page_width = page_rect.width
    page_height = page_rect.height

    # Convert PDF coordinates to pixel coordinates
    x0 = int(LEFT_MARGIN_CUTOFF * SCALE) - PADDING_LEFT
    y0 = int(q_y_top * SCALE) - PADDING_TOP
    x1 = int(page_width * SCALE) - PADDING_RIGHT
    y1 = int(content_bottom * SCALE) + PADDING_BOTTOM

    # Clamp to image bounds
    img_w, img_h = page_img.size
    x0 = max(0, x0)
    y0 = max(0, y0)
    x1 = min(img_w, x1)
    y1 = min(img_h, y1)

    if x1 <= x0 or y1 <= y0:
        return None

    cropped = page_img.crop((x0, y0, x1, y1))

    # Convert to numpy for whitespace trimming
    arr = np.array(cropped)

    # Trim bottom whitespace
    bottom_idx = trim_whitespace_bottom(arr)
    top_idx = trim_whitespace_top(arr)

    if bottom_idx <= top_idx:
        return None

    trimmed = cropped.crop((0, top_idx, cropped.width, bottom_idx))
    return trimmed


def resize_to_target_width(img, target_width=TARGET_WIDTH):
    """Resize image to target width while maintaining aspect ratio."""
    if img.width == 0:
        return img
    ratio = target_width / img.width
    new_height = int(img.height * ratio)
    if new_height == 0:
        return img
    return img.resize((target_width, new_height), Image.LANCZOS)


def add_white_background(img):
    """Ensure the image has a white background (no transparency)."""
    if img.mode == "RGBA":
        background = Image.new("RGB", img.size, (255, 255, 255))
        background.paste(img, mask=img.split()[3])
        return background
    elif img.mode != "RGB":
        return img.convert("RGB")
    return img


# ---------------------------------------------------------------------------
# Main extraction logic
# ---------------------------------------------------------------------------

def extract_questions_from_pdf(pdf_path):
    """
    Extract all MCQ questions from a single PDF file.
    Returns list of (q_num, PIL.Image) tuples.
    """
    doc = fitz.open(pdf_path)
    results = []
    seen_q_nums = set()

    print(f"\n  Processing: {os.path.basename(pdf_path)}")
    print(f"  Pages: {doc.page_count}")

    for page_idx in range(doc.page_count):
        page = doc[page_idx]
        page_rect = page.rect

        # Find question number positions on this page
        questions = find_question_positions(page)

        if not questions:
            continue

        # Render the page at high DPI
        pix = page.get_pixmap(dpi=DPI)
        page_img = Image.open(io.BytesIO(pix.tobytes("png")))
        page_img = add_white_background(page_img)

        # Process each question
        for i, (q_num, q_y_top) in enumerate(questions):
            # Skip duplicates (sometimes the same number appears in headers)
            if q_num in seen_q_nums:
                continue

            # Determine bottom boundary
            if i + 1 < len(questions):
                next_q_y_top = questions[i + 1][1]
            else:
                next_q_y_top = None

            content_bottom = find_content_bottom(
                page, q_y_top, next_q_y_top, page_rect.height
            )

            # Crop the question
            cropped = crop_question(page_img, q_y_top, content_bottom, page_rect)
            if cropped is None or cropped.height < 10:
                print(f"    WARNING: Q{q_num} crop was empty, skipping")
                continue

            # Resize to uniform width
            final_img = resize_to_target_width(cropped)
            results.append((q_num, final_img))
            seen_q_nums.add(q_num)

    doc.close()
    return results


def process_all_pdfs(pdf_dir):
    """Process all PDF files in the given directory."""
    pdf_files = sorted([
        f for f in os.listdir(pdf_dir)
        if f.lower().endswith(".pdf")
    ])

    if not pdf_files:
        print("No PDF files found in:", pdf_dir)
        return

    print(f"Found {len(pdf_files)} PDF files to process.")

    for pdf_file in pdf_files:
        pdf_path = os.path.join(pdf_dir, pdf_file)

        # Create output subfolder named after the PDF (without extension)
        base_name = os.path.splitext(pdf_file)[0]
        output_dir = os.path.join(pdf_dir, base_name)
        os.makedirs(output_dir, exist_ok=True)

        # Extract questions
        results = extract_questions_from_pdf(pdf_path)

        if not results:
            print(f"  No questions extracted from {pdf_file}")
            continue

        # Save images
        for q_num, img in results:
            img_path = os.path.join(output_dir, f"Q{q_num:02d}.png")
            img.save(img_path, "PNG", optimize=True)

        print(f"  Exported {len(results)} questions to: {output_dir}")

    print("\nDone!")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    process_all_pdfs(PDF_DIR)
