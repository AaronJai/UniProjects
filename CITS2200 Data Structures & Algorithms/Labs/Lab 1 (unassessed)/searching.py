def cube_root(x):
    """Find the cube root of `x` using binary search.

    Does not use exponentiation operator (**).

    Args:
        x: The value for which to find the cube root.

    Returns:
        The cube root of `x`, accurate to 7 decimal places.
    """
    # Define the boundaries based on whether x is positive or negative
    if x >= 1:
        low = 0
        high = x
    elif x < 0:
        low = x
        high = 0
    else:  # x is between 0 and 1
        low = 0
        high = 1

    # Define the precision
    precision = 1e-7

    # Binary search
    while True:
        mid = (low + high) / 2
        mid_cubed = mid * mid * mid

        # If the cube of mid is close enough to x, return mid
        if abs(mid_cubed - x) < precision:
            return round(mid, 7)

        # Adjust the boundaries based on the comparison of mid^3 and x
        if mid_cubed < x:
            low = mid
        else:
            high = mid



def lower_bound(xs, x):
    """Find the number of elements less than a value in a sorted list.

    Args:
        xs: A list sorted in ascending order.
        x: The value to search for.

    Returns:
        The number of elements less than `x` in `xs`.
    """
    # loop through list to see what index the value is in. find length of values up to x (exclusive)
    
    # index = 0
    # for i in xs:
    #     if i == x:
    #         index = xs.index(i)
    #         break

    # return len(xs[:index])

    left = 0
    right = len(xs) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if xs[mid] >= x:
            right = mid - 1
        else:
            left = mid + 1
    return left


def upper_bound(xs, x):
    """Find the number of elements less than or equal to a value in a sorted list.

    Args:
        xs: A list sorted in ascending order.
        x: The value to search for.

    Returns:
        The number of elements less than or equal to `x` in `xs`.
    """
    # same as above but inclusive  

    # index = 0
    # for i in xs:
    #     if i == x:
    #         index = xs.index(i)
    #         break

    # return len(xs[:index+1])

    # left = 0
    # right = len(xs) - 1
    # while left <= right:
    #     mid = left + (right - left) // 2
    #     if xs[mid] <= x:    # if statement flipped
    #         right = mid - 1
    #     else:
    #         left = mid + 1
    # return left

    left = 0
    right = len(xs) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if xs[mid] <= x:
            left = mid + 1
        else:
            right = mid - 1
    return left

