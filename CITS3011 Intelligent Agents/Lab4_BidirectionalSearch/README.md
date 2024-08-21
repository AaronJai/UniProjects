# Lab 4: Bidirectional Search

You are a renowned treasure hunter on a quest to find a hidden artefact. The artefact is rumored to be located in a complex labyrinth, and you have been tasked with developing an algorithm to find the shortest path from the entrance of the labyrinth to the artefact. To accomplish this, you decide to use **bidirectional search**, a technique that explores the labyrinth from both the entrance and the artefact simultaneously.

The input will consist of a labyrinth represented as a two-dimensional grid, where each cell can be either a wall (represented by `'#'`) or an empty space (represented by `'.'`). The entrance will be denoted by the character `'E'`, and the artefact by the character `'A'`. The dimensions of the labyrinth will not exceed 100 rows and 100 columns.

In `search.py` you can find an empty function `bidirectional_search(labyrinth)`. Implement this function so that it uses a **bidirectional search** to find the shortest path from the entrance of the labyrinth to the artefact.

Your algorithm should return the path as a list of coordinates. Each pair of coordinates should be in the format `(row, column)`, a pair of integers. If there is no path from the entrance to the artefact, you should return `None`.

**Paths should start at E and end at A.**

How to run the tester, in a terminal:
```
python3 test.py
```
