import numpy as np
import pyvista as pv
from pyvistaqt import BackgroundPlotter
from constantes import atom_colors
from raios_atomicos import atomic_radii
from estrutura import generate_cell_corners, get_faces, fractional_to_cartesian
from exportacao import exportar_cif
from importacao import ler_cif

plotter = None
matrix_vars = None
f0, f1, f2 = None, None, None
atom_positions = np.array([])
atom_symbols = []
lattice_vectors_orig = np.eye(3)
all_atoms = np.array([])
replicated_symbols = []
replication_flags = {}
show_atoms = None
red_cell_actor = None
red_cell_surfaces = None

def inicializar_variaveis(matrix, t_f0, t_f1, t_f2, show, replicas):
    global matrix_vars, f0, f1, f2, show_atoms, replication_flags
    matrix_vars = matrix
    f0, f1, f2 = t_f0, t_f1, t_f2
    show_atoms = show
    replication_flags = replicas

def carregar_cif(path):
    global atom_positions, atom_symbols, lattice_vectors_orig
    atom_positions, atom_symbols, lattice_vectors_orig = ler_cif(path)
    desenhar_plot(True)

def gerar_replicas_para_abranger(atom_positions, atom_symbols, lattice_vectors, target_vectors, target_origin):
    search_range = range(-2, 3)
    all_atoms = []
    V_inv = np.linalg.inv(target_vectors)
    eps = 1e-5

    for i in search_range:
        for j in search_range:
            for k in search_range:
                offset = i * lattice_vectors[0] + j * lattice_vectors[1] + k * lattice_vectors[2]
                for pos, sym in zip(atom_positions, atom_symbols):
                    shifted_pos = pos + offset
                    rel_pos = shifted_pos - target_origin
                    frac = np.dot(rel_pos, V_inv)
                    frac = np.clip(frac, 0 - eps, 1 + eps)  # Corrigido
                    if np.all((frac >= 0) & (frac <= 1)):
                        all_atoms.append((shifted_pos, sym))
    return all_atoms

def exportar_regiao():
    global all_atoms, replicated_symbols
    T = np.array([[var.get() for var in row] for row in matrix_vars])
    trans_vectors = T @ lattice_vectors_orig
    trans_origin = fractional_to_cartesian(np.array([f0.get(), f1.get(), f2.get()]), lattice_vectors_orig)

    atoms_in_cell = gerar_replicas_para_abranger(atom_positions, atom_symbols, lattice_vectors_orig, trans_vectors, trans_origin)

    if atoms_in_cell:
        posicoes, simbolos = zip(*[(p - trans_origin, s) for p, s in atoms_in_cell])
        exportar_cif(posicoes, simbolos, trans_vectors)
        print(f"✅ Exportado {len(simbolos)} átomos para 'recorte.cif'")
    else:
        print("⚠️ Nenhum átomo dentro da célula transformada.")

def atualizar_celula_vermelha(*args):
    global red_cell_actor, red_cell_surfaces
    if not plotter or red_cell_actor is None or red_cell_surfaces is None:
        return

    T = np.array([[var.get() for var in row] for row in matrix_vars])
    trans_vectors = T @ lattice_vectors_orig
    trans_origin = fractional_to_cartesian(np.array([f0.get(), f1.get(), f2.get()]), lattice_vectors_orig)
    new_corners = generate_cell_corners(trans_vectors, trans_origin)
    new_faces = get_faces(new_corners)

    for surf, face_pts in zip(red_cell_surfaces, new_faces):
        face_pts = np.array(face_pts)
        updated_surf = pv.PolyData(face_pts).delaunay_2d()
        surf.deep_copy(updated_surf)
    plotter.render()

def desenhar_plot(force_redraw=False):
    global plotter, red_cell_actor, red_cell_surfaces, all_atoms, replicated_symbols

    if plotter is None:
        plotter = BackgroundPlotter()

    if force_redraw or red_cell_actor is None or red_cell_surfaces is None:
        plotter.clear()
        red_cell_actor = []
        red_cell_surfaces = []

        T = np.array([[var.get() for var in row] for row in matrix_vars])
        trans_vectors = T @ lattice_vectors_orig
        trans_origin = fractional_to_cartesian(np.array([f0.get(), f1.get(), f2.get()]), lattice_vectors_orig)
        orig_corners = generate_cell_corners(lattice_vectors_orig)

        def draw_box(corners, color, opacity=0.4):
            faces = get_faces(corners)
            surfaces = []
            for face in faces:
                face_pts = np.array(face)
                surf = pv.PolyData(face_pts).delaunay_2d()
                actor = plotter.add_mesh(surf, color=color, style='surface', opacity=opacity, show_edges=True)
                surfaces.append(surf)
            return surfaces

        draw_box(orig_corners, color='white')

        replicated_atoms = gerar_replicas_para_abranger(atom_positions, atom_symbols, lattice_vectors_orig, trans_vectors, trans_origin)
        if replicated_atoms:
            all_atoms, replicated_symbols = zip(*replicated_atoms)
            all_atoms = np.array(all_atoms)

            if show_atoms.get():
                for pos, sym in zip(all_atoms, replicated_symbols):
                    color = atom_colors.get(sym, 'gray')
                    radius = atomic_radii.get(sym, 0.3)
                    sphere = pv.Sphere(radius=radius, center=pos, theta_resolution=32, phi_resolution=32)
                    plotter.add_mesh(sphere, color=color, smooth_shading=True)
            else:
                all_atoms = np.array([])

        red_corners = generate_cell_corners(trans_vectors, trans_origin)
        faces = get_faces(red_corners)
        for face in faces:
            face_pts = np.array(face)
            surf = pv.PolyData(face_pts).delaunay_2d()
            actor = plotter.add_mesh(surf, color='red', style='surface', opacity=0.4, show_edges=True)
            red_cell_surfaces.append(surf)
            red_cell_actor.append(actor)
