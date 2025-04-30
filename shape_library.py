import numpy as np

def get_shape_json(shape_name):
    if shape_name == "circle":
        theta = np.linspace(0, 2 * np.pi, 100)
        x = np.cos(theta)
        y = np.sin(theta)
    elif shape_name == "square":
        x = [1, 1, -1, -1, 1]
        y = [1, -1, -1, 1, 1]
    elif shape_name == "triangle":
        x = [0, 1, -1, 0]
        y = [1, -1, -1, 1]
    else:
        return None

    return {"shape": shape_name, "points": list(zip(x, y))}
