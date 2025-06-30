import numpy as np
from ase.io import read

def ler_cif(file_path):
    atoms = read(file_path)
    posicoes = atoms.get_positions()
    simbolos = atoms.get_chemical_symbols()
    celula = np.array(atoms.get_cell())
    return posicoes, simbolos, celula