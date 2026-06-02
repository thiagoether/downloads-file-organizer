import os
import shutil

pasta_de_origem = r"C:\Users\Thiago Ether\Downloads"

pastas = {
    ".jpg": "Imagens",
    ".png": "Imagens",
    ".pdf": "PDFs",
    ".mp3": "Musicas",
    ".xlsx": "Planilhas",
    ".zip": "Compactados",
    ".rar": "Compactados",
    ".stl": "STL",
    ".exe": "Exeutavéis",
    ".iso": "Imagem ISO"
}

for arquivo in os.listdir(pasta_de_origem):

    caminho_arquivo = os.path.join(pasta_de_origem, arquivo)

    if os.path.isdir(caminho_arquivo):
        continue

    extensao = os.path.splitext(arquivo)[1].lower()

    if extensao in pastas:
        pasta_destino = os.path.join(
            pasta_de_origem,
            pastas[extensao]
        )

        os.makedirs(pasta_destino, exist_ok=True)

        shutil.move(
            caminho_arquivo,
            os.path.join(pasta_destino, arquivo)
        )

        print(f"{arquivo} movido para {pastas[extensao]}")