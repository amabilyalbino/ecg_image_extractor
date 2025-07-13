import cv2
import pytesseract
import os

input_folder = "imagens"
output_folder = "output"
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        path = os.path.join(input_folder, filename)
        img = cv2.imread(path)

        # Cortar apenas os primeiros 100 pixels (área da logo)
        top_slice = img[0:100, :]
        text = pytesseract.image_to_string(top_slice).lower()

        if ("neif" in text or "musse" in text) and len(text.strip()) > 5:
            print(f"Logo detectado em {filename}. Cortando.")
            cropped = img[100:, :]  # remove os primeiros 100px
        else:
            print(f"Nenhum logo detectado em {filename}. Mantendo.")
            cropped = img

        # Salvar no output mantendo o nome original
        cv2.imwrite(os.path.join(output_folder, filename), cropped)
