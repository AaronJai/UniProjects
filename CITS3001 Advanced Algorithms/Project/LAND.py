from collections import deque

def land(num_properties, size_limit, properties):
    
    dp = [float('inf')] * (num_properties + 1)
    dp[0] = 0
    

    deque_window = deque()
    
    # Iterate through properties
    for i in range(1, num_properties + 1):
        total_size = 0
        max_value = 0
        
        # Traverse backwards
        j = i
        while j > 0 and total_size + properties[j-1][1] <= size_limit:
            total_size += properties[j-1][1]
            max_value = max(max_value, properties[j-1][0])
            dp[i] = min(dp[i], dp[j-1] + max_value)
            j -= 1
        
        # Add curr property to deque
        deque_window.append((i, (max_value, properties[i-1][1])))
    
    return dp[num_properties]
    
    # if num_properties == 0:
    #     return 0

    # dp = [float('inf')] * (num_properties + 1)
    # dp[0] = 0  # base case

    # dq = deque()

    # left = 0
    # total_size = 0

    # for right in range(1, num_properties + 1):
    #     value, size = properties[right - 1]
    #     total_size += size

    #     # Remove elements from the left until the total size is within the limit
    #     while total_size > size_limit:
    #         total_size -= properties[left][1]
    #         left += 1

    #     # Maintain a decreasing deque of property values for max calculation
    #     while dq and properties[dq[-1]][0] <= value:
    #         dq.pop()

    #     dq.append(right - 1)

    #     # Remove deque elements outside the current window
    #     while dq[0] < left:
    #         dq.popleft()

    #     # Update dp for the current window
    #     dp[right] = min(dp[right], dp[left] + properties[dq[0]][0])

    # return dp[num_properties]


x = input().split()
num_properties, size_limit = int(x[0]), int(x[1])

properties = []
for _ in range(num_properties):
    value, size = map(int, input().split())
    properties.append((value, size))

print(land(num_properties, size_limit, properties))
