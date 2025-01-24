# 🌟 Maze Solver with AI

This project is a Python-based maze solver that utilizes AI search algorithms (DFS and BFS) to find a path through a maze. It visualizes the solution and the explored states both in the terminal and as a PNG image.

---

## 🧠 Inspiration
This project was inspired by the **CS50's AI Course**. Building upon the foundational concepts taught in the course, I added several improvements, including:
- ✅ Support for both DFS (Depth-First Search) and BFS (Breadth-First Search).
- ✅ Enhanced flexibility and modularity in the code.
- ✅ Additional error handling and input validation.
- ✅ Improved visualization options for better understanding of the solving process.

---

## 🚀 Features
- 🔍 Solves mazes using AI search algorithms (DFS or BFS).
- 🖼 Displays the solution path and explored states visually in the terminal.
- 📷 Outputs a PNG image of the maze with the solution and explored states.
- 🛠 Modular design, allowing easy extensibility and readability.
- 🔒 Handles various edge cases and validates input files.

---

## 📋 Prerequisites
1. **Python 3.6+**
2. **Pillow** library for generating images.

To install Pillow:
```bash
pip install pillow
```

---

## ⚙️ How to Use
### 🗂 Input Format
The maze should be provided as a text file with the following structure:
- `A` marks the **start** position.
- `B` marks the **goal** position.
- `█` or any other character represents a **wall**.
- Spaces (` `) represent **walkable paths**.

Example `maze.txt`:
```
A █   █
  █ █ B
  █    
```

### ▶️ Running the Program
Use the following command:
```bash
python maze.py maze.txt [dfs|bfs]
```

- `maze.txt`: Path to the maze file.
- `[dfs|bfs]`: (Optional) Choose the search algorithm:
  - `dfs`: Depth-First Search (default).
  - `bfs`: Breadth-First Search.

#### Example
```bash
python maze.py maze.txt bfs
```

### 📊 Output
1. **Terminal Output**: Displays the maze, solution path, and states explored.
2. **Image Output**: Generates a `maze.png` file with the solution and explored states:
   - **Red**: Start point (`A`).
   - **Green**: Goal point (`B`).
   - **Light Green**: Solution path.
   - **Orange**: Explored states.
   - **Gray**: Walls.

---

## 📂 Example
### Input Maze (`maze.txt`):
```
A █ █
    █ B
█ █   
```

### Running the Program
```bash
python maze.py maze.txt bfs
```

### Terminal Output:
```
Maze:
A███
   █B
█ █

Solving using BFS...
States Explored: 6
Solution:
A███
***█B
█ █  
```

### Image Output (`maze.png`):
- A visual representation of the maze with the solution path and explored states.

---

## 🔥 Improvements Added
### Compared to the CS50 AI Course:
1. **BFS Support**: In addition to DFS, this project supports BFS for optimal pathfinding.
2. **Flexible Frontier Class**: Unified `StackFrontier` and `QueueFrontier` into a single class, improving code maintainability.
3. **Visualization**:
   - Added the ability to output PNG images of the maze.
   - Highlighted solution paths and explored states in distinct colors.
4. **Error Handling**:
   - Validates input files for missing start/goal points or invalid characters.
   - Provides meaningful error messages for invalid usage.
5. **Command-Line Options**: Users can select the algorithm via command-line arguments.

---

## 🚀 Next Steps
Future improvements could include:
- 🔄 Support for additional algorithms like A* or Greedy Best-First Search.
- 🎥 Dynamic visualization of the solving process (step-by-step animation).
- 🛠 Interactive maze generation and solving interface.

---

## 💬 Acknowledgments
Special thanks to **CS50's AI Course** for providing the foundational concepts and inspiration for this project.

