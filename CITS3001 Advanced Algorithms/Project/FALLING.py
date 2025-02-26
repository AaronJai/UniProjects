def dfs(node, adj_list, visited):
    
    visited[node] = True
    count = 1 
    
    for neighbour in adj_list[node]:
        if not visited[neighbour]:
            count += dfs(neighbour, adj_list, visited)
    return count

def calculate_factors(D, R, relations):
    # Initialize adj list
    adj_list = {i: [] for i in range(1, D + 1)}
    
    # Build the adj list 
    for x, y in relations:
        adj_list[x].append(y)
    
    # Calculate factor for each domino
    factors = []
    for i in range(1, D + 1):
        visited = [False] * (D + 1)
        factors.append(dfs(i, adj_list, visited))
    
    return factors



D, R = map(int, input().split())
relationsip = [tuple(map(int, input().split())) for _ in range(R)]

factors = calculate_factors(D, R, relationsip)
print(" ".join(map(str, factors)))
