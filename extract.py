import fitz  # PyMuPDF
import os

pdf_path = "ecg.pdf"
output_folder = "imagens_extraidas"
os.makedirs(output_folder, exist_ok=True)

doc = fitz.open(pdf_path)
count = 0

for i, page in enumerate(doc):
    for img_index, img in enumerate(page.get_images(full=True)):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        image_filename = f"page_{i+1}_img_{img_index+1}.{image_ext}"
        with open(os.path.join(output_folder, image_filename), "wb") as f:
            f.write(image_bytes)
        count += 1

print(f"{count} imagens extraídas para a pasta '{output_folder}'")
