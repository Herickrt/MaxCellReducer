import sys
from importlib.util import find_spec

REQUIRED = {"numpy", "pyvista", "pyvistaqt", "ase"}

missing = [pkg for pkg in REQUIRED if find_spec(pkg) is None]

if missing:
    msg = (
        "As seguintes bibliotecas não foram encontradas:\n"
        + "\n".join(f"  • {pkg}" for pkg in missing)
        + "\n\nInstale executando:\n    pip install " + " ".join(missing)
    )
    print(msg)

    try:
        import tkinter as tk
        from tkinter import messagebox
        tk.Tk().withdraw()
        messagebox.showerror("Dependências ausentes", msg)
    except Exception:
        pass

    sys.exit(1)

if __name__ == "__main__":
    from splash import mostrar_splash
    mostrar_splash()

