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
    elif shape_name == "a":
        x = [-1, 0, 1, 0.5, -0.5]
        y = [-1, 1, -1, 0, 0]
    elif shape_name == "b":
        x = [-1, -1, 0.5, -1, 0.5, -1]
        y = [1, -1, -0.5, 0, 0.5, 1]
    elif shape_name == "c":
        theta = np.linspace(np.pi / 4, 7 * np.pi / 4, 50)
        x = np.cos(theta)
        y = np.sin(theta)
        x = np.insert(x, 0, [np.cos(np.pi / 4)])
        y = np.insert(y, 0, [np.sin(np.pi / 4)])
        x = np.append(x, np.cos(7 * np.pi / 4))
        y = np.append(y, np.sin(7 * np.pi / 4))
    else:
        return None

    return {"shape": shape_name, "points": list(zip(x, y))}
