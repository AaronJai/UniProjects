def insertion_sort(xs):
    """Sorts the given list using insertion sort.

    Args:
        xs: The list to be sorted.

    Returns:
        The list in ascending order.
    """
    # loop through list starting from element 1, check if previous element is larger & if so swap.
    for i in range(1, len(xs)):
        j = i

        while (j > 0 and xs[j-1] > xs[j]):
            xs[j-1], xs[j] = xs[j], xs[j-1]
            j -= 1
    return xs

def merge(lhs, rhs):
    """Merges a pair of sorted lists.

    Args:
        lhs: A sorted list to be merged with rhs.
        rhs: A sorted list to be merged with lhs.

    Returns:
        A sorted list containing all the elements of lhs and rhs.
    """
    # if element in one list is smaller, append to a list containing 'results' and remove element from original list.
    # if after appending theres still a remaining number, add rest to list.
    # remember to have while loop to see if lhs and rhs has elements

    result = []

    while (lhs and rhs):
        if lhs[0] < rhs[0]:
            result.append(lhs[0])
            lhs.pop(0)
        else:
            result.append(rhs[0])
            rhs.pop(0)
        
    if (lhs):
        result += lhs
    if (rhs):
        result += rhs
    
    return result



def merge_sort(xs):
    """Sorts the given list using merge sort.

    Args:
        xs: The list to be sorted.

    Returns:
        The list in ascending order.
    """

    # split list into halves. and recursively call those halves with the function to split them up more. Then return by putting those halves into merge function
    # find half by finding middle index to split into left and right.

    if len(xs) <= 1:
        return xs
    
    middle_index = len(xs) // 2
    left_split = xs[:middle_index]
    right_split = xs[middle_index:]
    
    left_sorted = merge_sort(left_split)
    right_sorted = merge_sort(right_split)

    return merge(left_sorted, right_sorted)

def binary_search(data, target, low, high):
    if low > high:
        return None
    else:
        mid = (low + high) // 2
        cube = data[mid] * data[mid] * data[mid]
        if cube == target:
            return data[mid]
        elif cube < target:
            return binary_search(data, target, mid + 1, high)
        else:
            return binary_search(data, target, low, mid - 1)
        

"""
def merge(lhs, rhs):
    result = []
    i, j = 0, 0

    while i < len(lhs) and j < len(rhs):
        if lhs[i] < rhs[j]:
            result.append(lhs[i])
            i += 1
        else:
            result.append(rhs[j])
            j += 1

    result.extend(lhs[i:])
    result.extend(rhs[j:])

    return result

def merge (S1, S2, S):
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i+j] = S1[i]
            i += 1
        else:
            S[i+j] = S2[j]
            j += 1
"""
# the pop element could degrade performance.
# extend appends elements 