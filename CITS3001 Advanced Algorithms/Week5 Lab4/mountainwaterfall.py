def mountainwaterfall(grid):
    R = len(grid)
    C = len(grid[0])
    visited = set()

    def dfs(r, c):
        if (r, c) in visited:
            return
        visited.add((r, c))

        # Flow down if possible
        if r + 1 < R and grid[r + 1][c] == '.':
            grid[r + 1][c] = '*'  # Correctly update the cell in the grid
            dfs(r + 1, c)
        
        # Flow left and right if blocked below
        if r + 1 < R and grid[r + 1][c] == 'o':
            # Flow left
            if c - 1 >= 0 and grid[r][c - 1] == '.':
                grid[r][c - 1] = '*'  # Correctly update the cell in the grid
                dfs(r, c - 1)
            # Flow right
            if c + 1 < C and grid[r][c + 1] == '.':
                grid[r][c + 1] = '*'  # Correctly update the cell in the grid
                dfs(r, c + 1)

    # Start DFS from each water cell
    for r in range(R):
        for c in range(C):
            if grid[r][c] == '*':
                dfs(r, c)

    # Print the final grid
    for row in grid:
        print(''.join(row))

# Reading input
R, C = map(int, input().split())
grid = [list(input()) for _ in range(R)]

# Run the mountainwaterfall function
mountainwaterfall(grid)
