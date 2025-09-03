Pacman AI — CS3368 Project 1
================================

Overview
--------
This repository contains the Pacman AI Project 1 (Search) based on the UC Berkeley Pacman projects. It includes implementations and tests for Depth-First Search (DFS), Breadth-First Search (BFS), Uniform Cost Search (UCS), and A* Search with heuristics.

All provided autograder tests currently pass (total: 50/50).

Requirements
------------
- Python 3.9–3.12
- No additional third-party dependencies

Quick start
-----------
Run the full autograder (no graphics):

```bash
python3 autograder.py --no-graphics
```

Run a specific question (e.g., q3):

```bash
python3 autograder.py -q q3 --no-graphics
```

Play Pacman with search agents
------------------------------
Run Pacman on a small maze with BFS:

```bash
python3 pacman.py -l tinyMaze -p SearchAgent -a fn=bfs
```

Run A* with Manhattan heuristic on a medium maze:

```bash
python3 pacman.py -l mediumMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```

More layouts are in `layouts/`. Use `--no-graphics` in autograder runs to disable the GUI.

Notes
-----
- The autograder has been updated to use `importlib` instead of the deprecated `imp` module for Python 3 compatibility.
- If you’re on macOS, `.DS_Store` files are ignored by git.

Repository
----------
GitHub: `https://github.com/ak55m/packman-AI.git`

Attribution
-----------
The Pacman AI projects were developed at UC Berkeley. See headers in source files for licensing and attribution details.


