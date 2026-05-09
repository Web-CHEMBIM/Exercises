from PyPDF2 import PdfReader
import os

start_chapter = 5
end_chapter = 24

print(f"Starting extraction for chapters {start_chapter} to {end_chapter}...")

for i in range(start_chapter, end_chapter + 1):
    input_filename = f'Chapter {i}.pdf'
    output_filename = f'Chapter_{i}_extracted.txt'
    
    if not os.path.exists(input_filename):
        print(f'Warning: {input_filename} not found, skipping.')
        continue
        
    try:
        reader = PdfReader(input_filename)
        text = ''
        for page in reader.pages:
            extracted_text = page.extract_text()
            if extracted_text:
                text += extracted_text + '\n\n'
        
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(text)
            
        print(f'Extracted Chapter {i}: {len(reader.pages)} pages to {output_filename}')
    except Exception as e:
        print(f'Error extracting {input_filename}: {e}')

print('Extraction complete.')
