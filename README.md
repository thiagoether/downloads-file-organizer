# Organizador de Arquivos da Pasta Downloads

Script em Python desenvolvido para organizar automaticamente os arquivos da pasta Downloads com base em suas extensões.

O objetivo do projeto é automatizar uma tarefa comum do dia a dia: manter a pasta de downloads organizada, separando arquivos em categorias como imagens, documentos, vídeos, áudios, planilhas e arquivos compactados.

Este projeto foi desenvolvido como parte dos meus estudos em Python, com foco em automação, manipulação de arquivos e organização de diretórios.

---

## Funcionalidades

- Organiza arquivos automaticamente por extensão
- Cria as pastas de destino caso não existam
- Suporta diversas categorias de arquivos
- Ignora diretórios existentes
- Fácil de personalizar e expandir
- Utiliza apenas bibliotecas nativas do Python

---

## Exemplo de Funcionamento

Antes:

```text
Downloads/
├── foto.jpg
├── relatorio.pdf
├── musica.mp3
├── filme.mp4
├── arquivo.zip
```

Depois:

```text
Downloads/
├── Imagens/
│   └── foto.jpg
│
├── Documentos/
│   └── relatorio.pdf
│
├── Áudios/
│   └── musica.mp3
│
├── Vídeos/
│   └── filme.mp4
│
└── Compactados/
    └── arquivo.zip
```

---

## Tecnologias Utilizadas

- Python 3
- os
- shutil

---

## Como Funciona

O script realiza os seguintes passos:

1. Percorre todos os arquivos da pasta Downloads.
2. Identifica a extensão de cada arquivo.
3. Verifica a categoria correspondente.
4. Cria a pasta de destino, caso necessário.
5. Move o arquivo para a pasta correta.

---

## Categorias Suportadas

Exemplos de categorias organizadas pelo script:

| Categoria | Extensões |
|------------|------------|
| Imagens | .jpg, .jpeg, .png, .gif |
| Documentos | .pdf, .docx, .txt |
| Planilhas | .xlsx, .csv |
| Áudios | .mp3, .wav |
| Vídeos | .mp4, .avi |
| Compactados | .zip, .rar, .7z |

Novas extensões podem ser adicionadas facilmente alterando o dicionário de categorias no código.

---

## Estrutura do Projeto

```text
downloads-file-organizer/
│
├── file_organizer.py
├── README.md
└── requirements.txt
```

---

## Conhecimentos Aplicados

Este projeto permitiu praticar conceitos importantes de programação, incluindo:

- Manipulação de arquivos e diretórios
- Automação de tarefas
- Estruturas condicionais
- Organização de código
- Bibliotecas nativas do Python
- Interação com o sistema operacional

---

## Possíveis Melhorias Futuras

- Monitoramento automático da pasta Downloads em tempo real
- Interface gráfica (GUI)
- Arquivo de configuração personalizado
- Detecção de arquivos duplicados
- Sistema de logs

---

## Autor

Thiago  
Engenheiro da Computação | Estudante de Python para Automação e Dados
