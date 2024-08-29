from collections import defaultdict, deque

def find_longest_path(F, P, pairs):
    # Initialize graph and in-degree count
    graph = defaultdict(list)
    in_degree = [0] * (F + 1)
    
    # Build the graph
    for x, y in pairs:
        graph[y].append(x)
        in_degree[x] += 1
    
    # Kahn's algorithm for topological sorting and cycle detection
    queue = deque()
    dp = [0] * (F + 1)  # DP array to store the length of the longest path ending at each node
    
    # Start with all nodes that have in-degree of 0
    for i in range(1, F + 1):
        if in_degree[i] == 0:
            queue.append(i)
            dp[i] = 1  # Each node by itself counts as a path of length 1
    
    processed_nodes = 0
    
    while queue:
        node = queue.popleft()
        processed_nodes += 1
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
            dp[neighbor] = max(dp[neighbor], dp[node] + 1)
    
    # If not all nodes are processed, there is a cycle
    if processed_nodes < F:
        return -1
    
    # The result is the maximum value in dp array
    return max(dp)

# Read input
F = int(input().strip())
P = int(input().strip())
pairs = [tuple(map(int, input().split())) for _ in range(P)]

# Output the result
print(find_longest_path(F, P, pairs))
