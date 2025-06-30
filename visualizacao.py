from constantes import atom_colors

# Função para desenhar átomos na visualização 3D
def draw_atoms(ax, positions, symbols):
    for pos, sym in zip(positions, symbols):
        color = atom_colors.get(str(sym), 'gray')
        ax.scatter(*pos, color=color, s=50, edgecolors='k')