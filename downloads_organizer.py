import os
import shutil
import json

pasta_de_origem = r"C:\Users\Thiago Ether\Downloads"

with open("config.json", "r", encoding="utf-8") as arquivo:
    categorias = json.load(arquivo)


for arquivo in os.listdir(pasta_de_origem):

    caminho_arquivo = os.path.join(pasta_de_origem, arquivo)

    if os.path.isdir(caminho_arquivo):
        continue

    extensao = os.path.splitext(arquivo)[1].lower()

    if extensao in categorias:
        pasta_destino = os.path.join(
            pasta_de_origem,
            categorias[extensao]
        )

        os.makedirs(pasta_destino, exist_ok=True)

        shutil.move(
            caminho_arquivo,
            os.path.join(pasta_destino, arquivo)
        )

        print(f"{arquivo} movido para {categorias[extensao]}")