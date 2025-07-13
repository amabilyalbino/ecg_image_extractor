import cv2
import os

def ajustar_brilho_contraste(img, brightness=42, contrast=0):
    beta = brightness * 255 / 100  # brilho
    alpha = 1.0 + (contrast / 100)  # contraste
    return cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

def processar_imagens(pasta_entrada, pasta_saida):
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    for nome in os.listdir(pasta_entrada):
        if nome.lower().endswith(('.png', '.jpg', '.jpeg')):
            caminho = os.path.join(pasta_entrada, nome)
            imagem = cv2.imread(caminho)

            if imagem is None:
                print(f"Erro ao carregar imagem: {nome}")
                continue

            ajustada = ajustar_brilho_contraste(imagem, brightness=42, contrast=0)
            caminho_saida = os.path.join(pasta_saida, nome)
            cv2.imwrite(caminho_saida, ajustada)
            print(f"Imagem salva em: {caminho_saida}")

if __name__ == "__main__":
    entrada = "imagens_extraidas"
    saida = "imagens_tratadas"
    processar_imagens(entrada, saida)
