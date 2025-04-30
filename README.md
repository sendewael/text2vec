# Text 2 Vector with GloVe

![Python](https://img.shields.io/badge/python-3670A0?logo=python&logoColor=ffdd54)

An AI system that converts text descriptions of shapes into vectors using **GloVe 6B 100D** embeddings and allows users to visualize the shape, saving the vector data to a JSON file. The shapes currently supported are **circle**, **square**,**triangle**, can be turned into vectors and plotted. **letter A**, **letter B** and **letter C** can be plotted.

Developed as a proof-of-concept by Sen Dewael and Marnick Michielsen from Thomas More University (Geel, Belgium) in collaboration with KMITL (Bangkok, Thailand).

## Project Status 🚧

- ✅ **Text2Vec**: Convert shape names into GloVe embeddings and visualize shapes
- ✅ Shape plotting functionality (circle, square, triangle, letter A, letter B and letter C)
- ⚙️ **Future work**: Add more shapes and functionalities

> **Note:** This project is a proof-of-concept (POC). Some models or features may be incomplete or experimental.

---

# Folder Structure 📂

```bash
root/
├── cli_text2shape.py   # CLI tool for interacting with the shapes and vectors
├── glove_loader.py     # Loads the GloVe embeddings for text-to-vector conversion
├── shape_library.py    # Contains shape plotting logic (circle, square, triangle)
├── viewer.py           # Loads and visualizes saved JSON vectors
├── saved_vectors/      # Folder where JSON files are saved
```

# Features ✨

    🖌️ Text2Vec: Convert shape names ("circle", "square", "triangle") to GloVe vectors and plot corresponding shapes

    💾 Save vectors: Save the shape's name, vector values, and points to a JSON file in the saved_vectors/ directory

    🔄 Visualization: Visualize saved vectors and shapes using viewer.py

    ✍️ Extensibility: More shapes can be added to shape_library.py for plotting

# How It Works 🧠

    Text2Vec Conversion: Convert shape names (e.g., "circle") to vectors using GloVe 6B 100D.

    Shape Plotting: For recognized shapes like "circle", "square", or "triangle", the corresponding shape will be plotted.

    Save and Load Vectors: After plotting, save the shape's name, vector, and plotted points to a JSON file in saved_vectors/. Use viewer.py to load and visualize saved vectors later.

# Getting Started 🚀
## Installation

Clone the repository:
```bash
git clone https://github.com/your-username/drawing-finisher.git
cd drawing-finisher
```

Install the required packages:
```bash
pip install numpy matplotlib
```
### GloVe Embedding

This project uses the GloVe 6B 100D embeddings. You can download them from [here](https://nlp.stanford.edu/projects/glove/).
Once downloaded, unzip the file and place glove.6B.100d.txt in the project root directory.

### Running the CLI (cli_text2shape.py)

To generate vectors for shapes and view them:
```bash
python cli_text2shape.py
```
The program will:

    Ask you to input a shape name (e.g., circle, square, triangle).

    Plot the shape corresponding to the name (if recognized).

    Ask whether you'd like to save the shape's vector and plot data as a JSON file in the saved_vectors/ directory.

### Loading and Visualizing Saved Vectors (viewer.py)

To visualize any saved shape vectors, run the viewer.py script:
```bash
python viewer.py
```
You will be prompted to enter the file path of the saved JSON vector file. The corresponding shape will be plotted.
# Example Usage 🧑‍💻
### Running the CLI and generating vectors:
```bash
$ python cli_text2shape.py
Enter a shape name (circle, square, triangle): circle
```
This will plot a circle and ask if you want to save the vector.
### Visualizing a saved vector:
```bash
$ python viewer.py
Enter path to saved JSON vector file: saved_vectors/circle.json
```
This will load the saved vector and plot the corresponding circle.
# Future Improvements 🔮

    Add more shapes to shape_library.py (e.g., hexagon, pentagon, etc.)

    Implement more sophisticated shape detection and vectorization

    Develop a graphical interface (GUI or web-based)

# Contributors 👥

    Sen Dewael

    Marnick Michielsen
