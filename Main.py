import pyautogui
import time
import threading
import customtkinter as ctk
import keyboard

# Variáveis globais para controle das automações
running_clicker = False
running_spacebar = False

# Função para adicionar mensagens ao log
def log_message(message):
    log_textbox.insert("end", message + "\n")
    log_textbox.yview('end')  # Rolagem automática para o final

# Função para pressionar 'E' por 3 segundos e começar a clicar
def press_e_and_click():
    global running_clicker
    running_clicker = True
    update_status_label()
    log_message("E + Click automation started.")
    #app.iconify()  # Minimizar a janela
    while running_clicker:
        # Pressionar e segurar 'E' por 3 segundos
        pyautogui.keyDown('e')
        time.sleep(3)
        pyautogui.keyUp('e')

        # Iniciar os cliques com intervalo mínimo
        for _ in range(10):  # Ajuste o número de cliques conforme necessário
            if not running_clicker:
                break
            pyautogui.click()
            time.sleep(0.1)  # Intervalo mínimo entre os cliques

        # Simular um tempo de descanso
        time.sleep(10)  # Ajuste esse tempo conforme a necessidade
    log_message("E + Click automation stopped.")

# Função para pressionar a barra de espaço em intervalos
def press_spacebar():
    global running_spacebar
    running_spacebar = True
    update_status_label()
    log_message("Spacebar automation started.")
    #app.iconify()  # Minimizar a janela
    while running_spacebar:
        pyautogui.press('space')
        time.sleep(0.1)  # Intervalo mínimo entre as ativações
    log_message("Spacebar automation stopped.")

# Função para iniciar a automação de clicar
def start_clicker():
    threading.Thread(target=press_e_and_click).start()

# Função para parar a automação de clicar
def stop_clicker():
    global running_clicker
    running_clicker = False
    update_status_label()

# Função para iniciar a automação de pressionar barra de espaço
def start_spacebar():
    threading.Thread(target=press_spacebar).start()

# Função para parar a automação de barra de espaço
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
    status_label.configure(text=" | ".join(status))

# Função para verificar teclas de atalho
def check_hotkeys():
    while True:
        if keyboard.is_pressed('ctrl+shift+2'):
            if running_clicker:
                stop_clicker()
                log_message("Hotkey Ctrl+Shift+2: Stopped E + Click automation.")
            else:
                start_clicker()
                log_message("Hotkey Ctrl+Shift+2: Started E + Click automation.")
        if keyboard.is_pressed('ctrl+shift+4'):
            if running_spacebar:
                stop_spacebar()
                log_message("Hotkey Ctrl+Shift+5: Stopped Spacebar automation.")
            else:
                start_spacebar()
                log_message("Hotkey Ctrl+Shift+5: Started Spacebar automation.")
        time.sleep(0.1)

# Configurando a aparência da interface com customtkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Criando a interface gráfica com customtkinter
app = ctk.CTk()
app.title('Roblox Gym Automation')
app.geometry('600x700')

# Rótulo de título
title_label = ctk.CTkLabel(app, text="Roblox Gym Automation", font=("Arial", 20, "bold"))
title_label.pack(pady=10)

# Frame para botões de automação de 'E' e clique
frame_clicker = ctk.CTkFrame(app)
frame_clicker.pack(pady=10)

btn_start_clicker = ctk.CTkButton(frame_clicker, text='Start E + Click', command=start_clicker)
btn_start_clicker.grid(row=0, column=0, padx=10, pady=5)

btn_stop_clicker = ctk.CTkButton(frame_clicker, text='Stop E + Click', command=stop_clicker)
btn_stop_clicker.grid(row=0, column=1, padx=10, pady=5)

# Frame para botões de automação de barra de espaço
frame_spacebar = ctk.CTkFrame(app)
frame_spacebar.pack(pady=10)

btn_start_spacebar = ctk.CTkButton(frame_spacebar, text='Start Spacebar', command=start_spacebar)
btn_start_spacebar.grid(row=0, column=0, padx=10, pady=5)

btn_stop_spacebar = ctk.CTkButton(frame_spacebar, text='Stop Spacebar', command=stop_spacebar)
btn_stop_spacebar.grid(row=0, column=1, padx=10, pady=5)

# Rótulo para mostrar status das funções
status_label = ctk.CTkLabel(app, text="E + Click: Inactive | Spacebar: Inactive", font=("Arial", 12))
status_label.pack(pady=10)

# Textbox para exibir o log
log_textbox = ctk.CTkTextbox(app, height=400)
log_textbox.pack(pady=20, padx=20)
log_textbox.insert("end", "Instructions: Use Ctrl + Shift + 2 to start/stop the E + Click automation.\n")
log_textbox.insert("end", "Use Ctrl + Shift + 5 to start/stop the Spacebar automation.\n")
log_textbox.insert("end", "Use the buttons above to control the automations manually.\n\n")
log_textbox.yview('end')

# Rodapé
footer_label = ctk.CTkLabel(app, text="Automation Script for Roblox", font=("Arial", 12))
footer_label.pack(pady=10)

# Iniciar a verificação de teclas de atalho em uma nova thread
threading.Thread(target=check_hotkeys, daemon=True).start()

# Iniciar a interface gráfica
app.mainloop()
