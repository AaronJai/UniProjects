def max_sum_subarray_naive(xs: list[int]) -> int:
    best = 0  # Can always take empty subarray
    # Try every candidate xs[lwr:upr]
    for lwr in range(len(xs)):
        for upr in range(lwr + 1, len(xs) + 1):
            # Add up the candidate
            total = 0
            for i in range(lwr, upr):
                total += xs[i]
            # Keep track of the best
            best = max(best, total)
    return best

# Read input
input()
x = list(map(int, input().split()))

print(max_sum_subarray_naive(x))