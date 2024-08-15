"""
to find all squares within a range [L, R], you only need to consider values of k where k^2 ≤ R.
the largest possible k that satisfies this is sqrt(R)
e.g., if R is 100, the largest possible K to satisfy sqrt(R) is 10.

similarly for others:
cube: k^3 ≤ R,
sqube: k^6 ≤ R

complexity:
square: O(sqrt(R))
cube: O(^3sqrt(R))
sqube: O(^6sqrt(R))

but the first one dominates
"""

def inkysqubes(xs):
    L, R = xs[0], xs[1]
    
    # Count squares
    square_count = 0
    k = 1
    while k**2 <= R:
        if L <= k**2 <= R:
            square_count += 1
        k += 1
    
    # Count cubes
    cube_count = 0
    k = 1
    while k**3 <= R:
        if L <= k**3 <= R:
            cube_count += 1
        k += 1
    
    # Count squbes
    sqube_count = 0
    k = 1
    while k**6 <= R:
        if L <= k**6 <= R:
            sqube_count += 1
        k += 1
    
    result = str(square_count) + " " + str(cube_count) + " " + str(sqube_count)
    return result

x = list(map(int, input().split()))

print(inkysqubes(x))
