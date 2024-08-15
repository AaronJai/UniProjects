## Lab 3

## Counting Primes in O(N^2)
Go to the DOMjudge server (http://domjudge.gozz.au/) select lab3 and look at "countprimesmall". To solve this problem you will need to write a naive algorithm to count the number of primes under a threshold. You are aiming for a complexity of O(N^2) if the threshold is N. Recall that a number is prime if there is no number (other than 1 and itself) that divides it.

Reminder: You can check if x divides y using the modulo operator.
Hint: You can brute force this. Try every number up to the threshold. Then, for a each number, check if it's a prime by trying all possible divisors from 2 to x-1, where x is the number we are checking for primality.

## Counting Primes in O(N sqrt N)
Next, look at "countprimesmedium". This problem is the same but the bounds have increased. If you submit your O(N^2) solution you should get a TIMELIMIT verdict. A faster algorithm is needed. For this version of the question, you are aiming for a complexity of O(N sqrt N), that is, N times the square root of N. Try to speed up the inner loop that checks if a number is prime.

Hint 1: In the O(N^2) algorithm, each time we found a divisor d, we actually find two divisors, since x/d must also divide x. Can you use this obervation to end the loop early?

Hint 2: At what point does d become larger than x/d as we iterate through increasing values for d?

Note that this is an interesting case of an algorithm that has two loops but is not O(N^2)! Counting the number of loops isn't always a good guide to time complexity!

## Counting Primes in O(N log N)
Next, look at "countprimeslarge". Again, the problem is the same but the bounds have increased further. Both prior solutions should get TIMELIMIT. Your target complexity for this problem is O(N log N). Your algorithm should comprise two nested loops, but with a very different structure to before. An important piece of information to achieve the right complexity relates to the harmonic series. Specifically, 1+(1/2)+(1/3)+...+1/N = O(log N). This is a very useful and widely used piece of information in complexity analysis for algorithms. A good way to approach this problem is to first precompute a table that keeps track of how many divisors each number up to N has. The primes can be deduced by looking at this table. Note that you should avoid using a dictionary or set and instead use a list for this table. Dictionaries and sets are much slower than lists in Python and you may run into TIMELIMIT issues.

Note on time limit: If you go to the Problemset tab you can see that the time limit for this problem is unusually high at 18 seconds. This is because N was set high (5*10^7) to ensure that we could distinguish between O(N log N) and O(N sqrt N) solutions. It is actually still possible for very well optimized O(N sqrt N) solutions to pass even with these bounds! The reason for this is that O(N log N) and O(N sqrt N) are quite close until N becomes large, and there are many constant factor optimizations that are possible. Please keep in mind that the intent of this lab question is to develop an O(N log N) solution and understand the ideas behind it and the complexity analysis, not to heavily optimize an O(N sqrt N) solution so that it narrowly passes!

Note on PyPy: The DOMjudge server uses PyPy, an optimizing JIT compiler for Python, instead of the standard Python interpreter. This means it is likely to run much faster than it would on your machine, so if your local testing is taking a long time, it will still likely be fast enough on DOMjudge if your algorithm is noticably faster than the O(N sqrt N) solution. You can install PyPy on your own machine if you want to do a like-to-like comparison to the server.

If you are getting runtime error: DOMjudge only allows a maximum of 1GB memory usage. You may be going over the maximum allowed memory. This can happen if you are storing every divisor for every number, e.g., a list of lists. You only need to store a table with one value for each number!

Hint 1: You will need to change the structure of your algorithm. Instead of the outer loop looking at all numbers in the range and the inner loop checking if a number is prime, we will need to do something else. How many numbers can you rule out as not prime in a single loop through all the numbers?

Hint 2: The outer loop should go through all potential divisors, and the inner loop should go through multiples of that divisor and mark numbers as not prime. What is the complexity of this?

Hint 3: Following from the last hint, the total work done by the inner loop is N/2 when checking for divisor 2, N/3 when checking for divisor 3, and so on. Can you see how this can be analysed using the harmonic series?

(Optional) Extension: There is an even faster algorithm for doing this called the Sieve of Erastosthenes. It is recommended to fully understand the O(N log N) algorithm before looking at this. There are many variants of this algorithm, but the standard one has a complexity of O(N log log N). The "log log N" part means we take the log twice, i.e., log(log(N)), so it grows much slower than log N. This is a very fast algorithm! Understanding the complexity can be tricky and relies on knowing that the sum of primes up to a prime N (1/2+1/3+1/5+...+1/N) is O(log log N). However, you can see that the algorithm makes several clever optimizations over the O(N log N) version.

## Inky Squbes
Look at the "inkysqubes" problem on DOMjudge. This is a problem borrowed from the South Pacific ICPC 2021 Divisional Contest. It is not about counting primes, but uses several of the same ideas, particularly around the complexity analysis. Observe that R<=10^9, which means our target complexity must be better than O(N). In fact, the target complexity is O(sqrt N).

Hint 1: How many squares are there less than some R?

Hint 2: There are at most sqrt(R) squares! Since R <= 10^9, that's only about 30,000.

Hint 3: You can use a similar analysis for the number of cubes. There are at most R^(1/3), i.e., the cube root of R. This is even fewer than the number of squares.

Hint 4: You can count number of squbes by making a set of squares and cubes and taking the intersection. Alternatively, you can observe that a number x is a square if y*y=x, a cube is y^3=x, and a sqube if y^6=x.