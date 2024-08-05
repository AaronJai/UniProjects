"""
max_crossing_sum Function:

Computes the maximum sum of a subarray that crosses the midpoint. It does this by finding the maximum sum subarray ending at the midpoint and the maximum sum subarray starting just after the midpoint, then combining these sums.

divide_and_conquer Function:

Recursively divides the array into halves until the base case of a single element is reached.
Combines the results of the left half, right half, and the crossing subarray to get the overall maximum sum subarray.

Complexity:
    Divide: splitting = O(log N)
    Conquer: each level of recursion processes O(N) elements to find the maximum crossing sum
    Combine: combin
"""


def max_sum_subarray_divide_conquer(xs: list[int]) -> int:
    
    def max_crossing_sum(arr, left, mid, right):
        # Include elements on left of mid
        left_sum = float('-inf')
        current_sum = 0
        for i in range(mid, left - 1, -1):
            current_sum += arr[i]
            left_sum = max(left_sum, current_sum)
        
        # Include elements on right of mid
        right_sum = float('-inf')
        current_sum = 0
        for i in range(mid + 1, right + 1):
            current_sum += arr[i]
            right_sum = max(right_sum, current_sum)
        
        return left_sum + right_sum

    def divide_and_conquer(arr, left, right):
        if left == right:
            return max(0, arr[left])  # Base case: single element

        mid = (left + right) // 2
        left_max = divide_and_conquer(arr, left, mid)
        right_max = divide_and_conquer(arr, mid + 1, right)
        cross_max = max_crossing_sum(arr, left, mid, right)

        return max(left_max, right_max, cross_max)

    return divide_and_conquer(xs, 0, len(xs) - 1)

# Read input
input()
x = list(map(int, input().split()))

print(max_sum_subarray_divide_conquer(x))