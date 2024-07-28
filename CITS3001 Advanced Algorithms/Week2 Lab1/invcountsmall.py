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

input() 

x = list(map(int, input().split()))
print(count_inversions(x))