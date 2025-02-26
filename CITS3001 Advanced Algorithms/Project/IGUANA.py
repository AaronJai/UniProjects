import heapq

"""Use A* since we know the start and end points."""

# def heuristic(x, y, n):
#     # Using Manhattan distance to the bottom-right corner
#     return abs(n - 1 - x) + abs(n - 1 - y)

# def iggy_instructions(n, grid):
#     directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
#     # implementation inspired from Int.Agents lab
#     # PQ for A* (instruction count, heuristic cost, x, y, prev_direction)
#     pq = [(0, heuristic(0, 0, n), 0, 0, -1)] 
    
#     # Minimum instructions table
#     dp = [[float('inf')] * n for _ in range(n)]
#     dp[0][0] = 0
    
#     while pq:
#         count, _, x, y, prev_direction = heapq.heappop(pq)
        
#         # return result if reached end
#         if x == n - 1 and y == n - 1:
#             return count
        
#         # go through the directions
#         for i, (dx, dy) in enumerate(directions):
#             nx = x + dx
#             ny = y + dy
            
#             # Check if the next cell is within bounds and not blocked
#             if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == '.':
                
#                 if i != prev_direction:
#                     new_count = count + 1
#                 else:
#                     new_count = count
                
#                 # If theres better way to reach (nx, ny), add it to the pq
#                 if new_count < dp[nx][ny]:
#                     dp[nx][ny] = new_count
#                     estimated_cost = new_count + heuristic(nx, ny, n)
#                     heapq.heappush(pq, (new_count, estimated_cost, nx, ny, i))
    
#     return dp[n - 1][n - 1]





"""add dp into it"""
def heuristic(x, y, n):
    # Using Manhattan distance to the bottom-right corner
    return abs(n - 1 - x) + abs(n - 1 - y)

def iggy_instructions(n, grid):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    # PQ for A* (instruction count, heuristic cost, x, y, prev_direction)
    pq = [(0, heuristic(0, 0, n), 0, 0, -1)] 
    
    # dp table - track instructions and directions
    dp = [[[float('inf')] * 4 for _ in range(n)] for _ in range(n)]
    
    # Initialize the starting point for the directions
    for i in range(4):
        dp[0][0][i] = 0
    
    
    while pq:
        count, _, x, y, prev_direction = heapq.heappop(pq)
        
        # Return result if reached end
        if x == n - 1 and y == n - 1:
            return count
        
        # Go through the directions
        for i, (dx, dy) in enumerate(directions):
            nx = x + dx
            ny = y + dy
            
            # Check if the next cell is within bounds and not blocked
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == '.':
                
                if i != prev_direction:
                    new_count = count + 1
                else:
                    new_count = count
                
                # If there's a better way to reach (nx, ny) from this direction
                if new_count < dp[nx][ny][i]:
                    dp[nx][ny][i] = new_count
                    estimated_cost = new_count + heuristic(nx, ny, n)
                    heapq.heappush(pq, (new_count, estimated_cost, nx, ny, i))
    
    # Return the minimum instructions needed to reach the bottom-right corner
    return min(dp[n - 1][n - 1])

n = int(input().strip())
grid = [input().strip() for _ in range(n)]

print(iggy_instructions(n, grid))

# n = 5
# maze = [
#     ".....",
#     "####.",
#     ".....",
#     ".####",
#     "....."
# ]
# print("expected 5, got: ", iggy_instructions(n, maze))

# n = 5
# maze = [
#     ".....",
#     ".###.",
#     ".....",
#     ".####",
#     "....."
# ]
# print("expected 2, got: ", iggy_instructions(n, maze))

# n = 7
# maze = [
#     ".......",
#     "#.##.#.",
#     "#....#.",
#     "..####.",
#     "#....##",
#     "...#...",
#     "##....."
# ]
# print("expected 5, got: ", iggy_instructions(n, maze))

# n = 31
# maze = [
#     "...............................",
#     "...............................",
#     "...............................",
#     "...............................",
#     ".........##..##................",
#     ".....##..#.#.#.#................",
#     ".....#.#..#.#.#.#...######......",
#     "......#.#..##..#.#.#......##....",
#     "..##...##.#######.#...###...#...",
#     "..#.#.##.........#....#..#...#..",
#     "...#.#................#.#.....#",
#     "....#.................##......#",
#     "...#.......................##.#",
#     ".##....###....##...####......##",
#     ".#........#..#.....#..#......#.",
#     ".#.........#.#...#.#..#.....#..",
#     "#....#....#..#..#..###.....#...",
#     "#...#....#....#..#....#####....",
#     "#...#...#######...###...#......",
#     "#....##..#.....#..#.#...#......",
#     "#.....###......###.#.#.#.......",
#     ".##......##......#.#.#.........",
#     "...##......##.....#............",
#     ".....###.....##................",
#     "........####...#...............",
#     "............##..#..............",
#     "..............#..#.............",
#     "...............###.............",
#     "...............................",
#     "...............................",
#     "..............................."
# ]
# print("expected 11, got: ", iggy_instructions(n, maze))

# n = 1
# maze = [
#     "."
# ]
# print("expected 0, got: ", iggy_instructions(n, maze))