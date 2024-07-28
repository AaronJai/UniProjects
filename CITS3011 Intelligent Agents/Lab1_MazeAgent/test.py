import unittest

from maze_agent import MazeAgent

GRID_SIZE = 10

MAZES = [
'''...####...
#.#...#.#.
..#.#.#.#.
#.#.#.#.#.
..#.#.#.#.
#.#.#.#.#.
..#.#.#.#.
#...#...#.
#########.
..........''',
'''..........
.########.
.#......#.
.#.####.#.
.#.#..#.#.
.#.#..#.#.
.#.#..#.#.
.#.#....#.
.#.######.
.#........''',
'''.#...#....
...#......
...#..#...
...#......
...#......
..........
..........
......#...
..........
.#....#...''',
'''....#.....
..#.####.#
..####....
.......#..
..#.#...##
#....##...
.....#....
.#...#..##
......#..#
....##..#.''',
'''#.##......
#####.##.#
#..##.###.
........#.
#........#
....#.#...
###.##.#..
#.....##..
..#.#.#...
..##...#..''',
'''#..#.#.#..
##.#..##..
.#..##....
####.#...#
#####...#.
####..###.
#......###
..#..##...
#..#.#.#..
..####.#.#'''
]

class TestMazeAgent(unittest.TestCase):

    def stringToMaze(self, maze_str):
        lines = maze_str.split()
        return [[lines[y][x] == "." for x in range(GRID_SIZE)] for y in range(GRID_SIZE-1, -1, -1)]

    def runMaze(self, agent, maze):
        x = 9
        y = 9
        count = 0
        agent.reset()
        while count < 200 and ((x, y) != (0, 0)):
            count += 1
            move = agent.get_next_move(x, y)
            if (move == "U") and (y < GRID_SIZE-1) and maze[y+1][x]: y += 1
            elif (move == "D") and (y > 0) and maze[y-1][x]: y -= 1
            elif (move == "R") and (x < GRID_SIZE-1) and maze[y][x+1]: x += 1
            elif (move == "L") and (x > 0) and maze[y][x-1]: x -= 1
        return (x, y) == (0, 0)

    def test1(self):
        maze_str = MAZES[0]
        maze = self.stringToMaze(maze_str)
        self.assertTrue(self.runMaze(MazeAgent(), maze),
                        msg="did not reach end of maze within 200 moves\n"+maze_str)

    def test2(self):
        maze_str = MAZES[1]
        maze = self.stringToMaze(maze_str)
        self.assertTrue(self.runMaze(MazeAgent(), maze),
                        msg="did not reach end of maze within 200 moves\n"+maze_str)

    def test3(self):
        maze_str = MAZES[2]
        maze = self.stringToMaze(maze_str)
        self.assertTrue(self.runMaze(MazeAgent(), maze),
                        msg="did not reach end of maze within 200 moves\n"+maze_str)

    def test4(self):
        maze_str = MAZES[3]
        maze = self.stringToMaze(maze_str)
        self.assertTrue(self.runMaze(MazeAgent(), maze),
                        msg="did not reach end of maze within 200 moves\n"+maze_str)

    def test5(self):
        maze_str = MAZES[4]
        maze = self.stringToMaze(maze_str)
        self.assertTrue(self.runMaze(MazeAgent(), maze),
                        msg="did not reach end of maze within 200 moves\n"+maze_str)

    def test6(self):
        maze_str = MAZES[5]
        maze = self.stringToMaze(maze_str)
        self.assertTrue(self.runMaze(MazeAgent(), maze),
                        msg="did not reach end of maze within 200 moves\n"+maze_str)

if __name__ == "__main__":
    unittest.main()
