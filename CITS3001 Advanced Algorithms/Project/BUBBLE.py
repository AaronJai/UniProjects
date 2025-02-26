def bubble(num_bubbles, buckets, bubbles):
    
    if buckets >= num_bubbles:
        return 0
    
    # sort by size to minimise difference in each bucket
    bubbles.sort()
    
    # dynammic programming
    dp = [[float('inf')] * (buckets + 1) for _ in range(num_bubbles + 1)]
    
    # base case, score is 0
    dp[0][0]= 0
    
    scores = [[0] * num_bubbles for _ in range(num_bubbles)]
        
    for i in range(num_bubbles):
        for j in range(i, num_bubbles):
            scores[i][j] = (bubbles[j] - bubbles[i]) ** 2
    
    for i in range(1, num_bubbles + 1):
        for j in range(1, buckets + 1):
            for k in range(i):
                dp[i][j] = min(dp[i][j], dp[k][j - 1] + scores[k][i - 1])
                
    return dp[num_bubbles][buckets]



x = input().split()
num_bubbles, buckets = int(x[0]), int(x[1])
bubbles = [int(input()) for _ in range(num_bubbles)]

print(bubble(num_bubbles, buckets, bubbles))