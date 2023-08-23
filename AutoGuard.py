import tkinter as tk
from tkinter import ttk
import pyautogui
from datetime import datetime

class AutoGuard:
    def __init__(self, root):
        self.pending_tasks = []

        self.root = root
        self.root.title("AutoGuard - Hacker Simulator")
        self.root.configure(bg='black')  # Fondo negro

        # Estilo de los widgets
        self.textbox = tk.Text(self.root, height=8, width=40, bg='black', fg='lime', insertbackground='lime', wrap=tk.WORD)
        self.textbox.pack(pady=10)

        self.listbox = tk.Listbox(self.root, width=60, height=15, bg='black', fg='lime', selectbackground='lime')
        self.listbox.pack(pady=10)

        self.time_label = ttk.Label(self.root, text="Tiempo restante: 01:00", foreground='lime', background='black')
        self.time_label.pack(pady=5)

        self.progress = ttk.Progressbar(self.root, orient=tk.HORIZONTAL, length=300, mode='determinate')
        self.progress.pack(pady=10)

        self.clock_label = ttk.Label(self.root, text="", foreground='lime', background='black')
        self.clock_label.pack(pady=5)
        self.update_clock()

        self.is_active = False
        self.time_remaining = 60

        self.root.bind('<F12>', self.toggle_simulation)
        self.root.after(1000, self.update_simulation_time)

    def update_clock(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.clock_label.config(text=current_time)
        self.root.after(1000, self.update_clock)

    def simulate_behavior(self):

        
        # Movimiento aleatorio del cursor
        x, y = pyautogui.position()
        pyautogui.moveTo(x + 10, y + 10, duration=0.5)
        
        # Simulación de pulsaciones de teclas
        pyautogui.press('capslock')
        pyautogui.press('capslock')  # Pulsamos dos veces para que vuelva a su estado original

        # Escribir en el textbox
        self.textbox.insert(tk.END, f"Cursor movido a: {x + 10}, {y + 10}")
        self.textbox.insert(tk.END, "[*] Error: Acceso denegado!\n")
        self.textbox.insert(tk.END, "[*] Pulsado botón de bloqueo de mayúsculas!\n")


        # Animación de escritura en el listbox
        hacker_messages = [
            "[+] Intentando conexión a servidor...",
            "[!] Extrayendo credenciales...",
            "[*] Bypassing firewall...",
            "[+] ¡Acceso concedido!",
            "[*] Limpiando disco...",
            "[!] Detectando vulnerabilidades en el sistema...",
            "[+] Infectando red cercana...",
            "[*] Desactivando antivirus...",
            "[!] Descargando base de datos...",
            "[+] Inyectando malware en el sistema...",
            "[*] Rastreando ubicación del administrador...",
            "[!] Anulando protocolos de seguridad...",
            "[+] Extrayendo información financiera...",
            "[*] Desactivando alarmas...",
            "[!] Corrompiendo backups...",
            "[+] ¡Operación completada con éxito!",
            "[*] Borrando huellas digitales...",
            "[!] Desconectándose de la red...",
            "[+] ¡Hasta la próxima, sistema!"
        ]

        
        for i, message in enumerate(hacker_messages):
            delay_between_messages = 3000 * (i + 1)  # 3 segundos multiplicado por el índice
            self.root.after(delay_between_messages, self.type_message, message)
        
        # Limpiar el listbox después de mostrar todos los mensajes
        self.root.after(delay_between_messages + 3000, self.listbox.delete, 0, tk.END)

    def type_message(self, message):
        self.listbox.insert(tk.END, "")
        # Obtener el último índice del listbox
        last_index = self.listbox.size() - 1

        for index, char in enumerate(message):
            delay = int(2000 / len(message))  # Retraso para completar la frase en 2 segundos
            self.root.after(index * delay, lambda char=char, last_index=last_index: self.update_listbox(char, last_index))
            
        # Añadir un salto de línea después de completar cada mensaje
        # self.root.after(len(message) * delay, self.listbox.insert, tk.END, "")

    def update_listbox(self, char, last_index):
        current_text = self.listbox.get(last_index)
        updated_text = current_text + char
        self.listbox.delete(last_index)
        self.listbox.insert(last_index, updated_text)  
        self.listbox.see(tk.END)
  

    def toggle_simulation(self, event):
        self.is_active = not self.is_active
        if self.is_active:
            self.listbox.insert(tk.END, "[*] Modo Hacker activado")
        else:
            self.listbox.insert(tk.END, "[*] Modo Hacker desactivado")
            self.time_remaining = 60
            self.time_label.config(text=f"Tiempo restante: 01:00")
            self.progress['value'] = 0

    def update_simulation_time(self):
        if self.is_active:
            self.time_remaining -= 1
            self.progress['value'] = 100 - (self.time_remaining * 100 / 60)
            self.time_label.config(text=f"Tiempo restante: {self.time_remaining // 60:02}:{self.time_remaining % 60:02}")
            if self.time_remaining <= 0:
                self.simulate_behavior()
                self.time_remaining = 60
                self.progress['value'] = 0
        self.root.after(1000, self.update_simulation_time)

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoGuard(root)
    root.mainloop()

