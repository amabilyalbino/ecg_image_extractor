from PIL import Image
import os
import re

input_folder = "imagens_tratadas"
output_pdf = "ecg_final.pdf"

# Regex para extrair os números: page_XXX_pos_YYY
def extract_sort_key(filename):
    match = re.match(r"page_(\d+)_pos_(\d+)", filename)
    if match:
        page_num = int(match.group(1))
        pos_num = int(match.group(2))
        return (page_num, pos_num)
    else:
        return (9999, 9999)  # coloca no fim se não seguir o padrão

# Lista e ordena corretamente
image_files = sorted(
    [f for f in os.listdir(input_folder) if f.lower().endswith((".png", ".jpg", ".jpeg"))],
    key=extract_sort_key
)

# Carrega as imagens na ordem correta
images = [Image.open(os.path.join(input_folder, f)).convert("RGB") for f in image_files]

# Salva o PDF final
if images:
    images[0].save(output_pdf, save_all=True, append_images=images[1:])
    print(f"PDF final criado com sucesso: {output_pdf}")
else:
    print("Nenhuma imagem encontrada.")
