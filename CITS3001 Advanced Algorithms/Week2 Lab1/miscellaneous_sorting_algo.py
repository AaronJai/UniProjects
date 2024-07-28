def insertion_sort(xs: list): 
    # Iterate through prefix lengths 
    for l in range(1, len(xs)): 
        # Insert xs[l] into sorted prefix xs[0:l] 
        for i in range(l, 0, -1): 
            # xs[i] is element being inserted 
            if xs[i] < xs[i-1]: 
                # Wrong way around, swap them
                # Hint, this is an inversion!
                xs[i-1], xs[i] = xs[i], xs[i-1] 
            else: 
                # xs[i] is in the right spot 
                break 
        # xs[0:l+1] is now sorted 
    return xs # Modify this to return the inversion count instead of the sorted list

print(insertion_sort([3,2,5,4,1]))

def count_inversions(xs: list): 
    # Iterate through prefix lengths 
    count = 0
    for l in range(1, len(xs)): 
        # Insert xs[l] into sorted prefix xs[0:l]   
        for i in range(l, 0, -1): 
            # xs[i] is element being inserted 
            if xs[i] < xs[i-1]: 
                # Wrong way around, swap them
                # Hint, this is an inversion!
                xs[i-1], xs[i] = xs[i], xs[i-1] 
                count += 1
                
            else: 
                # xs[i] is in the right spot 
                break 
        # xs[0:l+1] is now sorted 
    return count # Modify this to return the inversion count instead of the sorted list

print(count_inversions([3,2,5,4,1]))

#################################################################################################################

def merge(lhs: list, rhs: list):
    result = []
    # lhs[li] and rhs[ri] are minimum elements not yet in result
    li, ri = 0, 0
    while li < len(lhs) and ri < len(rhs):
    # Append the lesser element
        if lhs[li] <= rhs[ri]:
            result.append(lhs[li])
            li += 1
        else:
            result.append(rhs[ri])
            ri += 1
    # Append any leftovers
    result.extend(lhs[li:] + rhs[ri:])
    return result

def merge_sort(xs: list):
    # Trivially sorted
    if len(xs) <= 1:
        return xs
    # Cut the list into halves and recursively sort
    mid = len(xs) // 2
    lhs = merge_sort(xs[:mid])
    rhs = merge_sort(xs[mid:])
    # Merge halves back together
    return merge(lhs, rhs)


###

def merge(lhs: list, rhs: list):
    result = []
    # lhs[li] and rhs[ri] are minimum elements not yet in result
    li, ri = 0, 0
    count = 0
    while li < len(lhs) and ri < len(rhs):
    # Append the lesser element
        if lhs[li] <= rhs[ri]:
            result.append(lhs[li])
            li += 1
            count += 1
        else:
            result.append(rhs[ri])
            ri += 1
            count += 1
    # Append any leftovers
    result.extend(lhs[li:] + rhs[ri:])
    return count

def inversion_merge_sort(xs: list):
    # Trivially sorted
    if len(xs) <= 1:
        return xs
    # Cut the list into halves and recursively sort
    mid = len(xs) // 2
    lhs = inversion_merge_sort(xs[:mid])
    rhs = inversion_merge_sort(xs[mid:])
    # Merge halves back together
    return merge(lhs, rhs)

print(count_inversions([3,2,5,4,1]))

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
    
    # call prev function to merge and count inversions
    merged, merge_inversions = merge_and_count(left, right)
    
    total_inversions = left_inversions + right_inversions + merge_inversions
    
    return total_inversions

