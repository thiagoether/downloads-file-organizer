# Organizador de Arquivos

Aplicação desenvolvida em Python para automatizar a organização de arquivos em diretórios específicos com base em suas extensões.

O projeto foi criado inicialmente para organizar a pasta Downloads, mas pode ser utilizado em qualquer diretório selecionado pelo usuário através da interface gráfica.

Além da organização automática dos arquivos, o sistema utiliza um arquivo de configuração JSON para definir categorias personalizadas e gera logs das operações realizadas.

---

## Funcionalidades

* Organização automática de arquivos por extensão
* Interface gráfica desenvolvida com Tkinter
* Seleção dinâmica da pasta a ser organizada
* Configuração de categorias através de arquivo JSON
* Criação automática das pastas de destino
* Registro das operações em arquivo de log
* Estrutura modularizada para facilitar manutenção e expansão
* Utilização exclusiva de bibliotecas nativas do Python

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

* Python 3
* Tkinter
* JSON
* os
* shutil
* datetime

---

## Como Funciona

1. O usuário seleciona uma pasta através da interface gráfica.
2. O sistema lê as categorias configuradas no arquivo `config.json`.
3. Cada arquivo é analisado de acordo com sua extensão.
4. A categoria correspondente é identificada.
5. Caso necessário, a pasta de destino é criada automaticamente.
6. O arquivo é movido para sua respectiva categoria.
7. A operação é registrada em um arquivo de log.

---

## Estrutura do Projeto

```text
downloads-file-organizer/
│
├── main.py
├── gui.py
├── organizer.py
├── config.json
├── README.md
│
└── logs/
    └── log.txt
```

---

## Configuração das Categorias

As categorias são definidas através do arquivo `config.json`.

Exemplo:

```json
{
    "Imagens": [".jpg", ".png", ".jpeg"],
    "Documentos": [".pdf", ".docx", ".txt"],
    "Áudios": [".mp3", ".wav"],
    "Vídeos": [".mp4", ".avi"],
    "Compactados": [".zip", ".rar"]
}
```

Novas categorias e extensões podem ser adicionadas sem modificar o código-fonte.

---

## Sistema de Logs

Todas as movimentações são registradas automaticamente.

Exemplo:

```text
2026-06-02 14:30:15 | foto.jpg -> Imagens
2026-06-02 14:30:16 | relatorio.pdf -> Documentos
```

---

## Conhecimentos Aplicados

Este projeto permitiu aplicar conceitos de:

* Manipulação de arquivos e diretórios
* Automação de tarefas
* Programação orientada à modularização
* Leitura de arquivos JSON
* Desenvolvimento de interfaces gráficas com Tkinter
* Registro de eventos (logs)
* Interação com o sistema operacional
* Organização e manutenção de código

---

## Melhorias Futuras

* Tratamento de arquivos duplicados
* Monitoramento automático de pastas em tempo real
* Estatísticas de arquivos processados
* Temas personalizados para a interface
* Geração de relatórios de organização

---

## Autor

Thiago Ether

Engenheiro da Computação | Python | Automação | Análise de Dados
