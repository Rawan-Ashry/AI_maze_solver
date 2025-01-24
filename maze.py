import sys
from collections import deque
from PIL import Image, ImageDraw

class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class Frontier:
    def __init__(self, use_stack=True):
        self.frontier = deque() if not use_stack else []
        self.use_stack = use_stack

    def add(self, node):
        if self.use_stack:
            self.frontier.append(node)
        else:
            self.frontier.appendleft(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("Empty frontier")
        if self.use_stack:
            return self.frontier.pop()
        else:
            return self.frontier.pop()


class Maze:
    def __init__(self, filename):
        # Read maze from file
        with open(filename) as f:
            contents = f.read()

        # Validate maze
        if contents.count("A") != 1 or contents.count("B") != 1:
            raise Exception("Maze must have one start point ('A') and one goal point ('B')")

        # Process maze dimensions
        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        # Initialize walls, start, and goal
        self.start = None
        self.goal = None
        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                if j >= len(contents[i]):
                    row.append(True)
                elif contents[i][j] == "A":
                    self.start = (i, j)
                    row.append(False)
                elif contents[i][j] == "B":
                    self.goal = (i, j)
                    row.append(False)
                elif contents[i][j] == " ":
                    row.append(False)
                else:
                    row.append(True)
            self.walls.append(row)

        if self.start is None or self.goal is None:
            raise Exception("Start or goal not found in maze")

        self.solution = None

    def print(self):
        solution = self.solution[1] if self.solution else None
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print("█", end="")
                elif (i, j) == self.start:
                    print("A", end="")
                elif (i, j) == self.goal:
                    print("B", end="")
                elif solution and (i, j) in solution:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()

    def neighbors(self, state):
        row, col = state
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1)),
        ]
        result = []
        for action, (r, c) in candidates:
            if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]:
                result.append((action, (r, c)))
        return result

    def solve(self, algorithm="dfs"):
        """Solves the maze using DFS or BFS."""
        self.num_explored = 0
        self.explored = set()

        # Select frontier based on algorithm
        use_stack = algorithm == "dfs"
        frontier = Frontier(use_stack=use_stack)
        frontier.add(Node(state=self.start, parent=None, action=None))

        while True:
            if frontier.empty():
                raise Exception("No solution")

            node = frontier.remove()
            self.num_explored += 1

            if node.state == self.goal:
                actions = []
                cells = []
                while node.parent:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return

            self.explored.add(node.state)
            for action, state in self.neighbors(node.state):
                if not frontier.contains_state(state) and state not in self.explored:
                    child = Node(state=state, parent=node, action=action)
                    frontier.add(child)

    def output_image(self, filename, show_solution=True, show_explored=False):
        cell_size = 50
        cell_border = 2

        img = Image.new(
            "RGBA",
            (self.width * cell_size, self.height * cell_size),
            "black"
        )
        draw = ImageDraw.Draw(img)

        solution = self.solution[1] if self.solution else None
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    fill = (40, 40, 40)
                elif (i, j) == self.start:
                    fill = (255, 0, 0)
                elif (i, j) == self.goal:
                    fill = (0, 171, 28)
                elif solution and show_solution and (i, j) in solution:
                    fill = (220, 235, 113)
                elif show_explored and (i, j) in self.explored:
                    fill = (212, 97, 85)
                else:
                    fill = (237, 240, 252)
                draw.rectangle(
                    [
                        (j * cell_size + cell_border, i * cell_size + cell_border),
                        ((j + 1) * cell_size - cell_border, (i + 1) * cell_size - cell_border),
                    ],
                    fill=fill,
                )
        img.save(filename)


if len(sys.argv) not in [2, 3]:
    sys.exit("Usage: python maze.py maze.txt [dfs|bfs]")

filename = sys.argv[1]
algorithm = sys.argv[2].lower() if len(sys.argv) == 3 else "dfs"
if algorithm not in ["dfs", "bfs"]:
    sys.exit("Invalid algorithm! Choose 'dfs' or 'bfs'.")

maze = Maze(filename)
print("Maze:")
maze.print()
print("Solving using", algorithm.upper(), "...")
maze.solve(algorithm=algorithm)
print("States Explored:", maze.num_explored)
print("Solution:")
maze.print()
maze.output_image("maze.png", show_explored=True)
