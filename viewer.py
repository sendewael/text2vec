import json
import os
import matplotlib.pyplot as plt

def load_and_plot(json_path):
    if not os.path.exists(json_path):
        print(f"❌ File not found: {json_path}")
        return

    with open(json_path, "r") as f:
        data = json.load(f)

    word = data.get("word", "Unknown")
    vector = data.get("vector")
    points = data.get("points")

    print(f"🔹 Word: {word}")
    print(f"🔹 Vector length: {len(vector)}")

    if points:
        x, y = zip(*points)
        plt.figure()
        plt.plot(x, y, 'b-')
        plt.fill(x, y, alpha=0.2)
        plt.title(f"Shape for '{word}'")
        plt.axis('equal')
        plt.grid(True)
        plt.show()
    else:
        print("ℹ️ No shape points in this JSON file, only the vector.")

if __name__ == "__main__":
    filename = input("Enter the name of the saved JSON file (e.g., 'circle.json'): ").strip()
    path = os.path.join("saved_vectors", filename)
    load_and_plot(path)
