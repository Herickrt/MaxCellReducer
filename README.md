# Max Cell Reducer

Visualizador interativo de células unitárias com suporte a transformação de base, translação, recorte periódico e exportação da nova célula reduzida. Desenvolvido em Python com PyVista e ASE.

---

## 🇧🇷 Descrição (Português)

### 📌 O que é?

O **Max Cell Reducer** é uma aplicação gráfica feita em Python que permite:
- Visualizar células unitárias a partir de arquivos `.cif`
- Transformar a célula por uma matriz 3×3
- Transladar a origem da célula transformada
- Aplicar condições periódicas de contorno para replicar átomos
- Exportar a célula reduzida para novo arquivo `.cif`

---

### 🧰 Requisitos

Antes de rodar, certifique-se de ter as seguintes bibliotecas instaladas:

```bash
pip install numpy pyvista pyvistaqt ase pillow
```

---

### ▶️ Como usar

1. Certifique-se de que todos os arquivos `.py` estejam na mesma pasta.
2. Execute o script `main.py`:

```bash
python main.py
```

3. A interface gráfica será aberta.
4. Clique em **"Carregar .cif"** para importar seu sistema.
5. Use os controles para:
   - Ajustar a matriz de transformação
   - Mover a origem da célula transformada
   - Duplicar em direções específicas (+X, -X, etc)
6. Clique em **"Exportar região transformada"** para gerar um novo `.cif`.

---

### 📂 Estrutura dos Arquivos

| Arquivo           | Função Principal                                   |
|-------------------|----------------------------------------------------|
| `main.py`         | Inicializa a aplicação                             |
| `interface.py`    | Cria a interface gráfica em tkinter                |
| `controle.py`     | Lógica central da aplicação                        |
| `estrutura.py`    | Funções de geometria (vetores, faces, etc.)        |
| `raios_atomicos.py` | Dicionário com raios atômicos                    |
| `constantes.py`   | Cores dos átomos por símbolo químico               |
| `importacao.py`   | Carrega arquivos `.cif` usando ASE                 |
| `exportacao.py`   | Exporta célula reduzida em `.cif`                  |
| `operacoes.py`    | Cálculos vetoriais e geométricos                   |
| `splash.py`       | (Opcional) Tela inicial com logo animado           |

---

## 🇺🇸 Description (English)

### 📌 What is it?

**Max Cell Reducer** is a Python-based GUI application for:

- Visualizing unit cells from `.cif` files
- Applying 3×3 matrix transformations
- Translating the origin of the transformed cell
- Replicating atoms with periodic boundary conditions (PBC)
- Exporting reduced unit cells to new `.cif` files

---

### 🧰 Requirements

Install the required libraries:

```bash
pip install numpy pyvista pyvistaqt ase pillow
```

---

### ▶️ How to use

1. Ensure all `.py` files are in the same folder.
2. Run:

```bash
python main.py
```

3. The GUI will open.
4. Click **"Carregar .cif"** to load your structure.
5. Use the controls to:
   - Modify the transformation matrix
   - Translate the origin
   - Duplicate along axes (+X, -X, etc)
6. Click **"Exportar região transformada"** to save the transformed region.

---

### 📂 File Overview

| File               | Description                                       |
|--------------------|---------------------------------------------------|
| `main.py`          | Entry point of the program                        |
| `interface.py`     | Builds the graphical interface (tkinter)          |
| `controle.py`      | Core logic and state management                   |
| `estrutura.py`     | Geometric functions for vectors and faces         |
| `raios_atomicos.py`| Dictionary of atomic radii                        |
| `constantes.py`    | Colors for chemical elements                      |
| `importacao.py`    | Imports `.cif` files using ASE                    |
| `exportacao.py`    | Exports reduced unit cells as `.cif`              |
| `operacoes.py`     | Mathematical and geometrical operations           |
| `splash.py`        | (Optional) Splash screen before loading the app   |

---

Desenvolvido por Herick.
