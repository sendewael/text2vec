import json
from glove_loader import load_glove_embeddings

# Predefined shapes and their labels (can be extended)
shape_names = ["circle", "square", "triangle"]

def generate_training_data(glove_path, output_path="shapes.json", vec_dim=100):
    glove = load_glove_embeddings(glove_path)
    data = []

    for shape in shape_names:
        if shape not in glove:
            print(f"Warning: '{shape}' not found in GloVe embeddings. Skipping.")
            continue

        entry = {
            "text": shape,
            "vector": glove[shape][:vec_dim].tolist()
        }
        data.append(entry)

    with open(output_path, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"✅ Saved {len(data)} shape vectors to {output_path}")

if __name__ == "__main__":
    generate_training_data("glove.6B.100d.txt")
