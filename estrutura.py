import numpy as np

def cell_vectors(a, b, c, alpha, beta, gamma):
    alpha, beta, gamma = np.radians([alpha, beta, gamma])
    v_a = np.array([a, 0.0, 0.0])
    v_b = np.array([b * np.cos(gamma), b * np.sin(gamma), 0.0])
    cx = c * np.cos(beta)
    cy = c * (np.cos(alpha) - np.cos(beta) * np.cos(gamma)) / np.sin(gamma)
    cz = np.sqrt(c**2 - cx**2 - cy**2)
    v_c = np.array([cx, cy, cz])
    return np.array([v_a, v_b, v_c])

def generate_cell_corners(vectors, origin=np.array([0, 0, 0])):
    corners = []
    for i in [0, 1]:
        for j in [0, 1]:
            for k in [0, 1]:
                point = origin + i * vectors[0] + j * vectors[1] + k * vectors[2]
                corners.append(point)
    return np.array(corners)

def get_faces(corners):
    return [[corners[i] for i in [0,1,3,2]],
            [corners[i] for i in [4,5,7,6]],
            [corners[i] for i in [0,1,5,4]],
            [corners[i] for i in [2,3,7,6]],
            [corners[i] for i in [0,2,6,4]],
            [corners[i] for i in [1,3,7,5]]]

def fractional_to_cartesian(frac, vectors):
    return frac[0] * vectors[0] + frac[1] * vectors[1] + frac[2] * vectors[2]