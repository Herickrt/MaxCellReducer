import tkinter as tk
from tkinter import ttk, filedialog
import controle

def iniciar_interface(root=None):
    if root is None:
        root = tk.Tk()
    root.title("Max Cell Reducer")

    show_atoms = tk.BooleanVar(value=True)
    replication_flags = {
        '+X': tk.BooleanVar(value=False), '-X': tk.BooleanVar(value=False),
        '+Y': tk.BooleanVar(value=False), '-Y': tk.BooleanVar(value=False),
        '+Z': tk.BooleanVar(value=False), '-Z': tk.BooleanVar(value=False),
    }

    # Frame principal de controles
    controls_frame = tk.Frame(root)
    controls_frame.pack(side=tk.TOP, fill=tk.BOTH, padx=10, pady=10)

    # =========================
    # 🔹 Grupo: Ações iniciais
    # =========================
    actions_frame = tk.LabelFrame(controls_frame, text="Ações")
    actions_frame.pack(side=tk.LEFT, padx=10, pady=10)

    def abrir_arquivo():
        caminho = filedialog.askopenfilename(filetypes=[("CIF files", "*.cif")])
        if caminho:
            controle.carregar_cif(caminho)

    btn_load = ttk.Button(actions_frame, text="Carregar .cif", command=abrir_arquivo)
    btn_load.pack(side=tk.TOP, fill=tk.X, pady=2)

    chk_atoms = ttk.Checkbutton(actions_frame, text="Mostrar átomos", variable=show_atoms,
                                command=lambda: controle.desenhar_plot(force_redraw=True))
    chk_atoms.pack(side=tk.TOP, fill=tk.X, pady=2)

    btn_exportar = ttk.Button(actions_frame, text="Exportar região transformada",
                              command=controle.exportar_regiao)
    btn_exportar.pack(side=tk.TOP, fill=tk.X, pady=5)

    # ==========================
    # 🔹 Grupo: Duplicar Eixos
    # ==========================
    dup_frame = tk.LabelFrame(controls_frame, text="Duplicar em")
    dup_frame.pack(side=tk.LEFT, padx=10, pady=10)
    for label, var in replication_flags.items():
        ttk.Checkbutton(dup_frame, text=label, variable=var,
                        command=controle.desenhar_plot).pack(side=tk.LEFT)

    # ================================
    # 🔹 Grupo: Matriz de Transformação
    # ================================
    matrix_frame = tk.LabelFrame(controls_frame, text="Matriz de Transformação")
    matrix_frame.pack(side=tk.LEFT, padx=15, pady=10)

    matrix_grid = tk.Frame(matrix_frame)
    matrix_grid.pack()
    matrix_vars = [[tk.DoubleVar(value=0.0 if i != j else 1.0) for j in range(3)] for i in range(3)]
    for i in range(3):
        for j in range(3):
            ttk.Entry(matrix_grid, textvariable=matrix_vars[i][j], width=6).grid(row=i, column=j, padx=2, pady=2)

    # ===================================
    # 🔹 Grupo: Vetores de Translação
    # ===================================
    trans_frame = tk.LabelFrame(controls_frame, text="Vetores de Translação")
    trans_frame.pack(side=tk.LEFT, padx=10, pady=10)

    f0, f1, f2 = tk.DoubleVar(value=0.0), tk.DoubleVar(value=0.0), tk.DoubleVar(value=0.0)
    for label, var in zip(['a', 'b', 'c'], [f0, f1, f2]):
        col = tk.Frame(trans_frame)
        col.pack(side=tk.LEFT, padx=5)
        tk.Label(col, text=label).pack()
        tk.Scale(col, variable=var, from_=-1.0, to=1.0, resolution=0.01,
                 orient=tk.HORIZONTAL, length=100).pack()

    # Inicialização do controle
    controle.inicializar_variaveis(matrix_vars, f0, f1, f2, show_atoms, replication_flags)

    for row in matrix_vars:
        for var in row:
            var.trace_add('write', lambda *args: controle.desenhar_plot())

    for var in [f0, f1, f2] + [var for row in matrix_vars for var in row]:
        var.trace_add('write', controle.atualizar_celula_vermelha)

    root.after(500, controle.desenhar_plot)
