import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

from organizer import organizar_arquivos

pasta_de_origem = ""


def selecionar_pasta():
    global pasta_de_origem

    pasta_de_origem = filedialog.askdirectory()

    if pasta_de_origem:
        label_pasta.config(
            text=f"Pasta selecionada:\n{pasta_de_origem}"
        )


def organizar():
    if not pasta_de_origem:

        messagebox.showwarning(
            "Aviso",
            "Selecione uma pasta primeiro."
        )

        return

    try:
        organizar_arquivos(
            pasta_de_origem
        )

        messagebox.showinfo(
            "Concluído",
            "Arquivos organizados com sucesso."
        )

    except Exception as erro:

        messagebox.showerror(
            "Erro",
            f"Ocorreu um erro:\n\n{erro}"
        )


def iniciar_interface():

    janela = tk.Tk()

    janela.title("File Organizer")

    janela.geometry("450x200")

    titulo = tk.Label(
        janela,
        text="Organizador de Arquivos",
        font=("Arial", 14)
    )

    titulo.pack(pady=10)

    global label_pasta

    label_pasta = tk.Label(
        janela,
        text="Nenhuma pasta selecionada",
        wraplength=450
    )

    label_pasta.pack(pady=10)

    botao_pasta = tk.Button(
        janela,
        text="Selecionar Pasta",
        command=selecionar_pasta,
        width=20
    )

    botao_pasta.pack(pady=5)

    botao_organizar = tk.Button(
        janela,
        text="Organizar",
        command=organizar,
        width=20
    )

    botao_organizar.pack(pady=5)

    janela.mainloop()