import tkinter as tk
from PIL import Image, ImageTk
import time
import threading
from interface import iniciar_interface
import os

def mostrar_splash():
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal inicialmente

    splash = tk.Toplevel(root)
    splash.overrideredirect(True)
    splash.configure(bg='white')

    try:
        img_path = os.path.join(os.path.dirname(__file__), "mcr.jpg")
        img = Image.open(img_path)
        img = img.resize((400, 400), Image.Resampling.LANCZOS)
        logo = ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Erro ao carregar imagem: {e}")
        splash.destroy()
        root.destroy()
        iniciar_interface()
        return

    canvas = tk.Canvas(splash, width=400, height=400, bg='white', highlightthickness=0)
    canvas.pack()
    canvas.create_image(200, 200, image=logo)

    splash.update_idletasks()
    w = splash.winfo_screenwidth()
    h = splash.winfo_screenheight()
    x = (w // 2) - (400 // 2)
    y = (h // 2) - (400 // 2)
    splash.geometry(f"+{x}+{y}")

    def iniciar_app():
        time.sleep(4)
        splash.destroy()
        root.deiconify()
        root.after(0, lambda: iniciar_interface(root))  # Executa iniciar_interface na thread principal

    threading.Thread(target=iniciar_app, daemon=True).start()
    root.mainloop()

