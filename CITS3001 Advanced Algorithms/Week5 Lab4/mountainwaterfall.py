def mountainwaterfall(grid):
    parsed_grid = store_grid(grid)
    
    if not parsed_grid['x']:
        return grid

    
    return parsed_grid


# from parsed input, store the grid characters in a 2D array
def store_grid(grid):
    positions = {'o': [],
                 'x': [],
                 '.': []}
    
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] in positions:
                positions[grid[r][c]].append((r, c))
    
    return positions



# Read input
x = input().split()
row, col = int(x[0]), int(x[1])

# Initialize grid by reading subsequent lines of input
grid = []
for _ in range(row):
    grid.append(input().strip())

# Store grid coordinates
coordinates = store_grid(grid)
