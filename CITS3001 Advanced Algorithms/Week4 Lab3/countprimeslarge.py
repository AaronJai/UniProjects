"""
    Initialize divisor_count List:
- Create a list where divisor_count[i] will store the number of divisors of i.

    Count Divisors:
- For each number i, increment the divisor count for all its multiples. This ensures that each number is correctly counted as a divisor for its multiples.
- The inner loop runs for each multiple of each number, which approximates the harmonic series

    Count Primes:
- A prime number will have exactly two divisors (1 and itself). Count how many numbers have exactly two divisors.
"""

def countprimeslarge(N):
    # Step 1: Initialize a list to count divisors
    divisor_count = [0] * (N + 1)
    
    # Step 2: Count divisors for each number
    for i in range(1, N + 1):
        for multiple in range(i, N + 1, i):     # hint 3 in readme.
            divisor_count[multiple] += 1
    
    # Step 3: Count numbers with exactly two divisors (i.e., prime numbers)
    count = 0
    for count in divisor_count:
        if count == 2:
            count += 1
    
    return count

# Read input
x = int(input().strip())
print(countprimeslarge(x))
