def knapsack(number_gpu: int, legal_limit: int, items: list[tuple[int, int]]) -> int:
    # Initialize dp array with infinity, except dp[0] = 0
    dp = [float('inf')] * (legal_limit + 1)
    dp[0] = 0
    
    for monetary_cost, environmental_cost in items:
        for w in reversed(range(environmental_cost, legal_limit + 1)):
            dp[w] = min(dp[w], dp[w - environmental_cost] + monetary_cost)
    
    # Find the maximum environmental cost with the minimum monetary cost
    for w in reversed(range(legal_limit + 1)):
        if dp[w] != float('inf'):
            return dp[w]
    
    return 0  # If no solution exists

# Reading input
number_gpu, legal_limit = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(number_gpu)]

# Get the result
result = knapsack(number_gpu, legal_limit, items)
print(result)

"""
// for environmental cost
def knapsack(number_gpu: int, legal_limit: int, items: list[tuple[int, int]]) -> int:
    # Initialize dp array with -1, indicating unattainable costs
    dp = [-1] * (legal_limit + 1)
    dp[0] = 0
    
    for monetary_cost, environmental_cost in items:
        for w in reversed(range(monetary_cost, legal_limit + 1)):
            if dp[w - monetary_cost] != -1:
                dp[w] = max(dp[w], dp[w - monetary_cost] + environmental_cost)
    
    # Find the maximum environmental cost with a finite monetary cost
    return max(dp)

"""