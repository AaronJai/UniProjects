# from collections import deque

# def flip(grid, R, C):
    
#     directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
#     visited = set()
#     scc_map = {}
#     flip_count = 0

#     def bfs(start_row, start_col, colour):
#         queue = deque()
#         queue.append((start_row, start_col))
#         visited.add((start_row, start_col))
#         scc = [(start_row, start_col)]  # Track all cells in the SCC

#         while queue:
#             row, col = queue.popleft()
#             for dr, dc in directions:
#                 new_row = row + dr
#                 new_col = col + dc
#                 if 0 <= new_row < R and 0 <= new_col < C:
#                     if (new_row, new_col) not in visited and grid[new_row][new_col] == colour:
#                         visited.add((new_row, new_col))
#                         queue.append((new_row, new_col))
#                         scc.append((new_row, new_col))  # Add cell to current SCC

#         return scc

#     def flip_scc(scc, new_colour):
#         for row, col in scc:
#             grid[row] = grid[row][:col] + new_colour + grid[row][col + 1:]

#     def find_scc_with_most_adjacent():
#         max_adj_scc_id = -1
#         max_adj_count = -1
#         for scc_id, adj_sccs in scc_map.items():
#             if len(adj_sccs) > max_adj_count:
#                 max_adj_scc_id = scc_id
#                 max_adj_count = len(adj_sccs)
#         return max_adj_scc_id

#     # Loop until grid is uniform
#     while True:
#         visited.clear()
#         scc_map.clear()

#         scc_id = 0
#         for row in range(R):
#             for col in range(C):
#                 if (row, col) not in visited:
#                     current_scc = bfs(row, col, grid[row][col])
#                     scc_map[scc_id] = current_scc
#                     scc_id += 1

#         if len(scc_map) == 1:  # All SCCs are uniform
#             break

#         # Find SCC with most adjacent SCCs
#         scc_to_flip_id = find_scc_with_most_adjacent()
#         scc_to_flip = scc_map[scc_to_flip_id]
#         target_colour = '.' if grid[scc_to_flip[0][0]][scc_to_flip[0][1]] == 'x' else 'x'

#         # Flip the SCC
#         flip_scc(scc_to_flip, target_colour)
#         flip_count += 1

#     return flip_count

"""
try with union-find method
1. identify the SCCs with BFS and we assign it an ID and store its colour
2. Adjacency list to see which components are adjacent
3. union find
 - tries to make it uniform.
 - union merges the parent sets (for each of the opposite SCCs, check if flipping can merge multiple in one go) and we count it
 - after that we'll have disjoint sets (SCCs) which need at least one flip each so just add the length to the count
"""

# from collections import deque

# def flip(grid, R, C):
#     directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

#     labels = [[-1 for _ in range(C)] for _ in range(R)]
#     component_id = 0                # identifier for each SCC
#     component_colours = []          # store the colour of each SCC
#     components = []                 # store the pixels of each SCC
    
#     # Build connected components
#     for i in range(R):
#         for j in range(C):
            
#             # if the pixel not yet visited
#             if labels[i][j] == -1:
#                 colour = grid[i][j]
#                 # for bfs
#                 queue = deque()
#                 queue.append((i, j))
#                 labels[i][j] = component_id
#                 component_pixels = []
                
#                 # BFS
#                 while queue:
#                     x, y = queue.popleft()
#                     component_pixels.append((x, y))
                    
#                     for dx, dy in directions:
#                         nx = x + dx
#                         ny = y + dy
                        
#                         # check boundaries
#                         if 0 <= nx < R and 0 <= ny < C:
#                             # if not visited and same colour add to queue
#                             if labels[nx][ny] == -1 and grid[nx][ny] == colour:
#                                 labels[nx][ny] = component_id
#                                 queue.append((nx, ny))
                                
#                 components.append(component_pixels)
#                 component_colours.append(colour)
#                 component_id += 1
                

#     num_components = component_id


#     # adj list
#     adj = []
#     for _ in range(num_components):
#         adj.append([])

#     for idx in range(num_components):
#         for x, y in components[idx]:
            
#             # check directions
#             for dx, dy in directions:
#                 nx, ny = x + dx, y + dy
                
#                 # check boundaries
#                 if 0 <= nx < R and 0 <= ny < C:     
#                     neighbor_idx = labels[nx][ny]
                    
#                     # add to adj list if part of different component & not added yet.
#                     if neighbor_idx != idx and neighbor_idx not in adj[idx]:
#                         adj[idx].append(neighbor_idx)

#     min_flips = float('inf')
    
    

#     # Try for both target colours
#     for target_colour in ['x', '.']:
#         # Store components of target colour
#         target_components = []
#         opposite_components = []
        
#         for i in range(num_components):
#             if component_colours[i] == target_colour:
#                 target_components.append(i)
#             else:
#                 opposite_components.append(i)

#         # initialise structure for union find
#         parent = []
#         for i in range(num_components):
#             parent.append(i)

#         # adapted from slides
#         def find(u):
#             # while parent[u] != u:
#             #     u = parent[u]
#             # return u
#             if parent[u] != u:
#                 parent[u] = find(parent[u])  # Path compression - makes the tree flatter therefore should be faster
#             return parent[u]

#         def union(u, v):
#             pu = find(u)
#             pv = find(v)
            
#             if pu != pv:
#                 parent[pu] = pv

#         flips = 0  # flip count

#         # For each opposite colour component, see if flipping it can merge target components
#         for idx in opposite_components:
#             neighbor_set = set()
#             for neighbor in adj[idx]:
#                 if component_colours[neighbor] == target_colour:
#                     neighbor_set.add(find(neighbor))
                    
#             if len(neighbor_set) >= 2:
#                 # Flipping this opposite colour component can merge target components
#                 flips += 1  # Flip this opposite component
#                 neighbor_list = list(neighbor_set)
#                 for i in range(1, len(neighbor_list)):
#                     union(neighbor_list[0], neighbor_list[i])

#         # Count number of disjoint sets among target components after merging
#         disjoint_sets = set()
#         for idx in target_components:
#             disjoint_sets.add(find(idx))

#         # update total flips - from after union and disjoint sets
#         total_flips = flips + len(disjoint_sets)
#         if total_flips < min_flips:
#             min_flips = total_flips

#     return min_flips

from collections import deque

# Directions for 8-connected neighbors
directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

def is_valid(x, y, R, C):
    return 0 <= x < R and 0 <= y < C

# BFS to find a connected component
def bfs(grid, R, C, x, y, visited):
    color = grid[x][y]
    queue = deque([(x, y)])
    visited[x][y] = True
    component = [(x, y)]
    
    while queue:
        cx, cy = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if is_valid(nx, ny, R, C) and not visited[nx][ny] and grid[nx][ny] == color:
                visited[nx][ny] = True
                queue.append((nx, ny))
                component.append((nx, ny))
    
    return component

# Function to count adjacent components
def count_adjacent_components(grid, R, C, component, visited_components):
    adj_colors = set()
    for x, y in component:
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, R, C) and (nx, ny) not in visited_components:
                adj_colors.add(grid[nx][ny])
    return len(adj_colors)

def flip(grid, R, C):
    visited = [[False] * C for _ in range(R)]
    components = []
    
    # Find all connected components
    for i in range(R):
        for j in range(C):
            if not visited[i][j]:
                component = bfs(grid, R, C, i, j, visited)
                components.append(component)
    
    if len(components) == 1:
        return 0  # Grid is already uniform
    
    visited_components = set()
    min_flips = 0
    
    # Iterate through the components and flip optimally
    while components:
        # Select the component that touches the most other components
        best_component = None
        max_adj = -1
        for component in components:
            adj_count = count_adjacent_components(grid, R, C, component, visited_components)
            if adj_count > max_adj:
                best_component = component
                max_adj = adj_count
        
        # Flip the selected component
        for x, y in best_component:
            grid[x][y] = 'x' if grid[x][y] == '.' else '.'
        
        # Mark the component as visited
        for x, y in best_component:
            visited_components.add((x, y))
        
        # Remove the flipped component from the list
        components.remove(best_component)
        
        # Increment flip count
        min_flips += 1
    
    return min_flips

# # Read input
# R, C = map(int, input().split())
# grid = [input().strip() for _ in range(R)]

# # Print the result
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
