import pyautogui
import time
import threading
import customtkinter as ctk
import keyboard

running_clicker = False
running_spacebar = False

# Função para pressionar 'E' por 3 segundos e começar a clicar
def press_e_and_click():
    global running_clicker
    running_clicker = True
    update_status_label()
    app.iconify()  # Minimizar a janela
    while running_clicker:
        # Pressionar e segurar 'E' por 3 segundos
        pyautogui.keyDown('e')
        time.sleep(3)
        pyautogui.keyUp('e')

        # Iniciar os cliques
        for _ in range(10):  # Ajuste o número de cliques
            if not running_clicker:
                break
            pyautogui.click()
            time.sleep(0.1)  # Intervalo entre os cliques

        # Simular tempo de caida
        time.sleep(5)

# Função para pressionar a barra de espaço
def press_spacebar():
    global running_spacebar
    running_spacebar = True
    update_status_label()
    app.iconify()  # Minimizar a janela
    while running_spacebar:
        pyautogui.press('space')
        time.sleep(0.1)  # Intervalo entre as ativações


def start_clicker():
    threading.Thread(target=press_e_and_click).start()


def stop_clicker():
    global running_clicker
    running_clicker = False
    update_status_label()


def start_spacebar():
    threading.Thread(target=press_spacebar).start()


def stop_spacebar():
    global running_spacebar
    running_spacebar = False
    update_status_label()

# Atualizar o status das funções ativas
def update_status_label():
    status = []
    if running_clicker:
        status.append("E + Click: Active")
    else:
        status.append("E + Click: Inactive")
    if running_spacebar:
        status.append("Spacebar: Active")
    else:
        status.append("Spacebar: Inactive")
    status_label.config(text=" | ".join(status))

# Função para verificar teclas de atalho
def check_hotkeys():
    while True:
        if keyboard.is_pressed('ctrl+shift+e'):
            if running_clicker:
                stop_clicker()
            else:
                start_clicker()
        if keyboard.is_pressed('ctrl+shift+s'):
            if running_spacebar:
                stop_spacebar()
            else:
                start_spacebar()
        time.sleep(0.1)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title('Roblox Gym Automation')
app.geometry('400x350')

title_label = ctk.CTkLabel(app, text="Roblox Gym Automation", font=("Arial", 20, "bold"))
title_label.pack(pady=20)

frame_clicker = ctk.CTkFrame(app)
frame_clicker.pack(pady=10)

btn_start_clicker = ctk.CTkButton(frame_clicker, text='Start E + Click', command=start_clicker)
btn_start_clicker.grid(row=0, column=0, padx=10, pady=5)

btn_stop_clicker = ctk.CTkButton(frame_clicker, text='Stop E + Click', command=stop_clicker)
btn_stop_clicker.grid(row=0, column=1, padx=10, pady=5)

frame_spacebar = ctk.CTkFrame(app)
frame_spacebar.pack(pady=10)

btn_start_spacebar = ctk.CTkButton(frame_spacebar, text='Start Spacebar', command=start_spacebar)
btn_start_spacebar.grid(row=0, column=0, padx=10, pady=5)

btn_stop_spacebar = ctk.CTkButton(frame_spacebar, text='Stop Spacebar', command=stop_spacebar)
btn_stop_spacebar.grid(row=0, column=1, padx=10, pady=5)

# Rótulo para mostrar status das funções
status_label = ctk.CTkLabel(app, text="E + Click: Inactive | Spacebar: Inactive", font=("Arial", 12))
status_label.pack(pady=20)

footer_label = ctk.CTkLabel(app, text="Automation Script for Roblox", font=("Arial", 12))
footer_label.pack(pady=20)

# Iniciar a verificação de teclas de atalho em uma nova thread
threading.Thread(target=check_hotkeys, daemon=True).start()

app.mainloop()
