def merge_and_count(lhs, rhs):
    result = []
    li, ri = 0, 0
    inversions = 0

    while li < len(lhs) and ri < len(rhs):
        if lhs[li] <= rhs[ri]:
            result.append(lhs[li])
            li += 1
        else:
            result.append(rhs[ri])
            ri += 1
            # inversion occurs when an element from rhs < lhs. since list is sorted, remaining elems in lhs > rhs[ri] leading to multiple inversions.
            inversions += len(lhs) - li  # Count inversions

    result.extend(lhs[li:])
    result.extend(rhs[ri:])
    
    return result, inversions

def inversion_merge_sort(xs):
    if len(xs) <= 1:
        return xs, 0

    mid = len(xs) // 2
    left, left_inversions = inversion_merge_sort(xs[:mid])
    right, right_inversions = inversion_merge_sort(xs[mid:])
    merged, merge_inversions = merge_and_count(left, right)
    
    total_inversions = left_inversions + right_inversions + merge_inversions
    
    return merged, total_inversions

# Read input
input()
x = list(map(int, input().split()))

# Sort the list and count inversions
sorted_list, inversions = inversion_merge_sort(x)

# Print the number of inversions
print(inversions)
