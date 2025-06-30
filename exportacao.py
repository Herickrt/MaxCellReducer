import os
from ase import Atoms
from ase.io import write

def exportar_cif(positions, symbols, cell, filename="reduced_cell.cif"):
    dir_base = os.path.dirname(os.path.abspath(__file__))  # Caminho da pasta onde está exportacao.py
    caminho_completo = os.path.join(dir_base, filename)

    atoms = Atoms(symbols=symbols, positions=positions, cell=cell, pbc=True)
    write(caminho_completo, atoms, format='cif')