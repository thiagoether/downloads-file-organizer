import os
import shutil
import json
from datetime import datetime

pasta_de_origem = r"C:\Users\Thiago Ether\Downloads"

with open("config.json", "r", encoding="utf-8") as arquivo:
    categorias = json.load(arquivo)


for arquivo in os.listdir(pasta_de_origem):

    caminho_arquivo = os.path.join(pasta_de_origem, arquivo)

    if os.path.isdir(caminho_arquivo):
        continue

    extensao = os.path.splitext(arquivo)[1].lower()

    categoria_encontrada = None

    for categoria, extensoes in categorias.items():
        if extensao in extensoes:
            categoria_encontrada = categoria
            break

    if categoria_encontrada:

        pasta_destino = os.path.join(
            pasta_de_origem,
            categoria_encontrada
        )

        os.makedirs(pasta_destino, exist_ok=True)

        shutil.move(
            caminho_arquivo,
            os.path.join(pasta_destino, arquivo)
        )
        hora = datetime.now()

        with open("log.txt", "a", encoding="utf-8") as log:
            log.write(
                f"{hora} | {arquivo} -> {categoria} \n"
            )

        print(f"{arquivo} movido para {categoria_encontrada}")