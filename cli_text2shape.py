from glove_loader import load_glove_embeddings
from shape_library import get_shape_json
import json
import matplotlib.pyplot as plt
import os

def plot_shape(shape_data):
    points = shape_data["points"]
    x, y = zip(*points)
    plt.figure()
    plt.plot(x, y, 'b-')
    plt.fill(x, y, alpha=0.2)
    plt.title(f"{shape_data['shape'].capitalize()} Shape")
    plt.axis('equal')
    plt.grid(True)
    plt.show()

def save_vector(word, vector, shape_data=None, out_dir="saved_vectors"):
    os.makedirs(out_dir, exist_ok=True)
    file_path = os.path.join(out_dir, f"{word}.json")

    save_data = {
        "word": word,
        "vector": vector.tolist()
    }

    if shape_data:
        save_data["points"] = shape_data["points"]

    with open(file_path, "w") as f:
        json.dump(save_data, f, indent=2)

    print(f"✅ Vector saved to {file_path}")

def main():
    print("🟦 Text2Vec CLI – type 'exit' to quit.")
    glove = load_glove_embeddings("glove.6B.100d.txt")

    while True:
        word = input("\nEnter any word (circle, square or traingle): ").strip().lower()
        if word == "exit":
            break

        vec = glove.get(word)
        shape = get_shape_json(word)  # Only returns shape if it's defined

        if vec is None:
            print(f"❌ '{word}' not found in GloVe vocabulary.")
            continue

        print(f"\n🔹 Vector for '{word}':\n{vec[:5]}... (len: {len(vec)})")

        if shape:
            print(f"🔹 Shape data found. Plotting...")
            plot_shape(shape)
        else:
            print("ℹ️ No shape data available for plotting.")

        save = input("💾 Save this vector to JSON? (y/n): ").strip().lower()
        if save == "y":
            save_vector(word, vec, shape_data=shape)

if __name__ == "__main__":
    main()
