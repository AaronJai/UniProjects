def max_sum_subarray_better(xs: list[int]) -> int:
    best = 0
    for lwr in range(len(xs)):
        total = 0
        # Incrementally grow subarray
        for i in range(lwr, len(xs)):
            total += xs[i]
            best = max(best, total)
    return best



# Read input
input()
x = list(map(int, input().split()))

print(max_sum_subarray_better(x))