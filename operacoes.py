import numpy as np

def generate_cell_corners(vectors, origin=np.zeros(3)):
    return np.array([
        origin + i*vectors[0] + j*vectors[1] + k*vectors[2]
        for i in [0,1] for j in [0,1] for k in [0,1]
    ])

def get_faces(corners):
    return [
        [corners[i] for i in [0,1,3,2]],
        [corners[i] for i in [4,5,7,6]],
        [corners[i] for i in [0,1,5,4]],
        [corners[i] for i in [2,3,7,6]],
        [corners[i] for i in [1,3,7,5]],
        [corners[i] for i in [0,2,6,4]]
    ]

def fractional_to_cartesian(frac, vectors):
    return np.dot(frac, vectors)

# exportacao.py
from ase.io import write
from ase import Atoms

def exportar_cif(positions, symbols, cell, filename="recorte.cif"):
    atoms = Atoms(symbols=symbols, positions=positions, cell=cell, pbc=True)
    write(filename, atoms, format='cif')

# visualizacao.py
from constantes import atom_colors

def draw_atoms(ax, positions, symbols):
    for pos, sym in zip(positions, symbols):
        color = atom_colors.get(str(sym), 'gray')
        ax.scatter(*pos, color=color, s=50, edgecolors='k')