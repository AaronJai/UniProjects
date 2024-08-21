import unittest, copy

from search import bidirectional_search

TEST_CASES = [
    (
        [
            ['#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', 'E', '.', '.', '.', '.', '.', '#'],
            ['#', '.', '#', '#', '#', '#', '.', '#'],
            ['#', '.', '#', '.', '#', '#', '.', '#'],
            ['#', '.', '#', '.', '.', '.', 'A', '#'],
            ['#', '.', '#', '#', '#', '#', '#', '#'],
            ['#', '.', '.', '.', '.', '.', '.', '#'],
            ['#', '#', '#', '#', '#', '#', '#', '#'],
        ],
        9,
    ),
    (
        [
            ['#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', '.', '.', '.', '.', 'E', '.', '#'],
            ['#', '.', '#', '#', '#', '#', '.', '#'],
            ['#', '.', '#', '.', '#', '#', '.', '#'],
            ['#', '#', '#', '.', '.', '.', '.', '#'],
            ['#', '.', '#', '#', '#', '#', '#', '#'],
            ['#', '.', '.', '.', 'A', '.', '.', '#'],
            ['#', '#', '#', '#', '#', '#', '#', '#'],
        ],
        0,
    ),
    (
        [
            ['#', '#', '#', '#'],
            ['#', 'E', '.', '#'],
            ['#', '.', '.', '#'],
            ['#', '#', '.', 'A'],
        ],
        5,
    ),
    (
        [
            ['E', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '#', '.'],
            ['#', '#', '#', '#', '#', '#', '#', '.', '#', '.'],
            ['.', '.', '.', '.', '.', '.', '#', '.', '#', '.'],
            ['.', '#', '#', '#', '#', '.', '#', '.', '#', '.'],
            ['.', '#', '.', '.', '#', '.', '#', '.', '#', '.'],
            ['.', '#', '#', '.', '#', '.', '#', '.', '#', '.'],
            ['.', '.', '.', '.', '#', '.', '#', '.', '#', '.'],
            ['.', '#', '#', '#', '#', '#', '#', '#', '#', 'A'],
        ],
        19,
    ),
    (
        [
            ['#', '#', '#', '#'],
            ['#', 'E', '#', '#'],
            ['#', '#', '#', '#'],
            ['#', '#', '#', 'A'],
        ],
        0,
    ),
    (
        [
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '#', '.'],
            ['#', '#', '#', '#', '#', '#', '#', '.', '#', '.'],
            ['.', '.', '.', '.', '.', '.', '#', '.', '#', '.'],
            ['.', '#', '#', '#', '#', '.', '#', '.', '#', '.'],
            ['.', '#', 'E', '.', '#', '.', '#', '.', '#', '.'],
            ['.', '#', '#', '.', '#', '.', '#', '.', '#', '.'],
            ['.', '.', '.', '.', '#', '.', '#', '.', '#', '.'],
            ['.', '#', '#', '#', '#', '#', '#', '#', '#', 'A'],
        ],
        0,
    ),
]

VALID_MOVES = {(0, -1), (0, 1), (-1, 0), (1, 0)}

class TestBidirectionalSearch(unittest.TestCase):

    def doTest(self, labyrinth, shortest_path_length):
        print("\nRunning {}".format(self._testMethodName))
        path = bidirectional_search(copy.deepcopy(labyrinth))
        print("path =", path)
        
        if shortest_path_length == 0:
            self.assertIsNone(path, "there is no path possible, so you should have returned None")
            return
        
        self.assertIsNotNone(path, "you returned None, but there is a valid path from E to A")
        self.assertGreater(len(path), 0, "path is empty")
        
        min_r, max_r = 0, len(labyrinth)-1
        min_c, max_c = 0, len(labyrinth[0])-1
        
        prev_r, prev_c = None, None
        for i, coords in enumerate(path):
            r, c = coords
            self.assertGreaterEqual(r, min_r, "coordinates ({}, {}) are not within labyrinth".format(r, c))
            self.assertLessEqual(r, max_r, "coordinates ({}, {}) are not within labyrinth".format(r, c))
            self.assertGreaterEqual(c, min_c, "coordinates ({}, {}) are not within labyrinth".format(r, c))
            self.assertLessEqual(c, max_c, "coordinates ({}, {}) are not within labyrinth".format(r, c))
            
            if i == 0:
                self.assertEqual(labyrinth[r][c], "E", "path must start from E")
            else:
                move = (r-prev_r, c-prev_c)
                self.assertTrue(move in VALID_MOVES, "going from ({}, {}) to ({}, {}) is not a valid move".format(prev_r, prev_c, r, c))
                
                if i == len(path)-1:
                    self.assertEqual(labyrinth[r][c], "A", "path must end at A")
                else:
                    self.assertNotEqual(labyrinth[r][c], "#", "path cannot go through walls")
                
            prev_r = r
            prev_c = c
        
        self.assertEqual(len(path), shortest_path_length, "shortest path is length {}, your path is length {}".format(shortest_path_length, len(path)))

    def test1(self):
        self.doTest(*TEST_CASES[0])
    
    def test2(self):
        self.doTest(*TEST_CASES[1])
    
    def test3(self):
        self.doTest(*TEST_CASES[2])
    
    def test4(self):
        self.doTest(*TEST_CASES[3])
    
    def test5(self):
        self.doTest(*TEST_CASES[4])
    
    def test6(self):
        self.doTest(*TEST_CASES[5])

if __name__ == "__main__":
    unittest.main()
