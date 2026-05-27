import tkinter as tk
from tkinter import messagebox

usuarios = {}

def cadastrar():

    nome = entrada_nome_cadastro.get()
    senha = entrada_senha_cadastro.get()

    # Verificar campos vazios
    if nome == "" or senha == "":
        messagebox.showerror(
            "Erro",
            "Preencha todos os campos"
        )
        return

    # Verificar se usuário já existe
    if nome in usuarios:

        messagebox.showerror(
            "Erro",
            "Usuário já existe"
        )

    else:

        # Salvar no dicionário
        usuarios[nome] = senha

        messagebox.showinfo(
            "Sucesso",
            "Usuário cadastrado!"
        )

        # Limpar campos
        entrada_nome_cadastro.delete(0, tk.END)
        entrada_senha_cadastro.delete(0, tk.END)

def login():

    nome = entrada_nome_login.get()
    senha = entrada_senha_login.get()

    # Verificar se usuário existe
    if nome in usuarios:

        # Verificar senha
        if usuarios[nome] == senha:

            messagebox.showinfo(
                "Sucesso",
                "Login realizado!"
            )

            abrir_home(nome)

        else:

            messagebox.showerror(
                "Erro",
                "Senha incorreta"
            )

    else:

        messagebox.showerror(
            "Erro",
            "Usuário não encontrado"
        )

# ==========================================
# ABRIR NOVA TELA
# ==========================================

def abrir_home(nome_usuario):

    home = tk.Toplevel()

    home.title("Página Principal")

    home.geometry("300x200")

    texto = tk.Label(
        home,
        text=f"Bem-vindo,\n{nome_usuario}!",
        font=("Arial", 16)
    )

    texto.pack(pady=50)

# ==========================================
# JANELA PRINCIPAL
# ==========================================

janela = tk.Tk()

janela.title("Sistema de Login")

janela.geometry("500x400")

# ==========================================
# TÍTULO LOGIN
# ==========================================

titulo_login = tk.Label(
    janela,
    text="LOGIN",
    font=("Arial", 18)
)

titulo_login.pack(pady=10)

# ==========================================
# LOGIN USUÁRIO
# ==========================================

entrada_nome_login = tk.Entry(janela)

entrada_nome_login.pack(pady=5)

entrada_nome_login.insert(0, "Nome")

# ==========================================
# LOGIN SENHA
# ==========================================

entrada_senha_login = tk.Entry(
    janela,
    show="*"
)

entrada_senha_login.pack(pady=5)

# ==========================================
# BOTÃO LOGIN
# ==========================================

botao_login = tk.Button(
    janela,
    text="Entrar",
    command=login
)

botao_login.pack(pady=10)

# ==========================================
# SEPARADOR
# ==========================================

linha = tk.Label(
    janela,
    text="--------------------------"
)

linha.pack(pady=10)

# ==========================================
# TÍTULO CADASTRO
# ==========================================

titulo_cadastro = tk.Label(
    janela,
    text="CADASTRO",
    font=("Arial", 18)
)

titulo_cadastro.pack(pady=10)

# ==========================================
# CADASTRO NOME
# ==========================================

entrada_nome_cadastro = tk.Entry(janela)

entrada_nome_cadastro.pack(pady=5)

entrada_nome_cadastro.insert(0, "Novo nome")

# ==========================================
# CADASTRO SENHA
# ==========================================

entrada_senha_cadastro = tk.Entry(
    janela,
    show="*"
)

entrada_senha_cadastro.pack(pady=5)

# ==========================================
# BOTÃO CADASTRAR
# ==========================================

botao_cadastro = tk.Button(
    janela,
    text="Cadastrar",
    command=cadastrar
)

botao_cadastro.pack(pady=10)

# ==========================================
# EXECUTAR PROGRAMA
# ==========================================

janela.mainloop()