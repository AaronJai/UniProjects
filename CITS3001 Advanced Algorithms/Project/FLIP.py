"""
https://codeforces.com/blog/entry/17974
inspiration taken from the above link
key part being:
'using BFS from any node (denote it as v1) find the farthest from v1 node (denote as v2), then run BFS from v2, choose the farthest node from v2 (call it v3). Nodes in the middle of the path between v2 and v3 are center of graph, distance between them is diameter. Radius of graph is half of diameter rounded up: (diam(G) + 1) / 2.'


"""

from collections import deque

         
def bfs(graph, start):
    visited = set([start])
    queue = deque([(start, 0)])  # (node, distance)
    farthest_node, max_distance = start, 0

    # normal bfs exploration visit all nodes
    while queue:
        node, dist = queue.popleft()    
        
        if dist > max_distance:
            farthest_node, max_distance = node, dist
            
        for neighbour in graph.get(node, []): # get all neighbours
            if neighbour not in visited:
                visited.add(neighbour)  # mark as visited
                queue.append((neighbour, dist + 1)) # continue
    
    return farthest_node, max_distance



def flip(grid, R, C):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    
    # Tracking the components
    visited = [[False for _ in range(C)] for _ in range(R)] 
    component_id = [[-1 for _ in range(C)] for _ in range(R)] 
    graph = {}  # for adj matrix
    current_id = 0
    
    
    # Explore connected pixels and assign IDs to them
    def explore_component(r, c, colour):
        queue = deque([(r, c)]) # bfs queue
        visited[r][c] = True
        component_id[r][c] = current_id
        
        while queue:
            x, y = queue.popleft()
            
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy 
                
                # check for boundaries, if already visited and if the colour is the same
                if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and grid[nx][ny] == colour:      
                    visited[nx][ny] = True # mark as visited
                    component_id[nx][ny] = current_id
                    queue.append((nx, ny))  # continue exploring
    
    
    # Assign component IDs for each connected region
    for i in range(R):
        for j in range(C):
            if not visited[i][j]: # if not visited it should be a new component
                explore_component(i, j, grid[i][j]) # explore the component
                current_id += 1 # move to next Id

    # Build adj matrix - to connect components next to each other
    for i in range(R):
        for j in range(C):
            comp = component_id[i][j]
            
            if comp not in graph:
                graph[comp] = set() # initialise the set of neighbours for the component
                
            for dx, dy in directions:  
                ni = i + dx
                nj = j + dy
                
                # check boundary and if neighbour is a different component (colour)
                if 0 <= ni < R and 0 <= nj < C and component_id[ni][nj] != comp:
                    graph[comp].add(component_id[ni][nj])
 
 

    start_node = 0  # Pick any component to start with but 0 works. could probs do random() too
    
    # logic from the link above
    v2, _ = bfs(graph, start_node) # get furthest node from from starting node
    v3, diameter = bfs(graph, v2) # find furthest node from that node
    
    # calculate
    radius = (diameter + 1) // 2
    
    
    return radius


# # Input reading and processing
# R, C = map(int, input().split())
# grid = [input().strip() for _ in range(R)]

# # Output the result
# print(flip(grid, R, C))


# Test 1
R = 6
C = 6
grid = [
    ".xx...",
    "xxx...",
    "....xx",
    "......",
    "xxxxxx",
    "......"
]
print("Test 1 result:", flip(grid, R, C))  # Expected output: 2

# Test 1 flipped
R = 6
C = 6
grid = [
    "x..xxx",
    "..xxxx",
    "xxxx..",
    "xxxxxx",
    "......",
    "xxxxxx"
]

print("Test 1 flipped result:", flip(grid, R, C))  # Expected output: 2


# Test 2
R = 2
C = 8
grid = [
    "..xx.xx.",
    "x..xxx.x"
]
print("Test 2 result:", flip(grid, R, C))  # Expected output: 2

# Test 3
R = 7
C = 8
grid = [
    "..xxxx..",
    ".x....x.",
    ".....x..",
    "....x...",
    "....x...",
    "........",
    "....x..."
]
print("Test 3 result:", flip(grid, R, C))  # Expected output: 1


# edge cases

R = 3
C = 3
grid = [
    "xxx",
    "xxx",
    "xxx"
]
print("All-black grid result:", flip(grid, R, C))  # Expected output: 0

R = 5
C = 5
grid = [
    "xx.x.",
    "x....",
    "..xx.",
    "....x",
    ".x.x."
]
print("Grid with many small regions result:", flip(grid, R, C))  # Expected output: 1

R = 4
C = 4
grid = [
    "x.x.",
    ".x.x",
    "x.x.",
    ".x.x"
]
print("Grid with diagonal connections result:", flip(grid, R, C))  # Expected output: 1

# Divrrs test
R = 4
C = 17
grid = [
    "xxxx.xx.....xx.xx",
    "..x.xx..x.x.x.x..",
    "..xx.xxx.x......x",
    "x..xxxx...xxx.x.."
]
print("Divrr result:", flip(grid, R, C))  # Expected output: 2
