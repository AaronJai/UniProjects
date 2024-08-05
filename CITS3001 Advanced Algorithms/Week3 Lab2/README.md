In this lab we will be looking at the Maximum Sum Subarray problem. This was mentioned in the Intro lecture. Formally, consider an array A of numbers. We want to find the subarray whose sum is the largest possible amoung all subarrays of A. Define a subarray as a contiguous subsequence of elements. For example, if A=[3,2,4,1,-4,2], then this is a subarray [3,2,4,1,-4,2], and so is this [3,2,4,1,-4,2]. However, this [3,2,4,1,-4,2] is not a subarray, because it is not contiguous. In this example, the maximum sum subarray is [3,2,4,1,-4,2]. Note that we define the empty subarray as having a sum of zero, so the maximum sum subarray of A=[-2,-3,-1] is the empty subarray and it has sum 0.

## Maximum Sum Subarray in O(N^2)
Please revise lecture 1, the intro lecture. In this lecture the maximum sum subarray problem is mentioned. First, an O(n^3) algorithm is introduced. Here is the code from the lecture.

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


This is a naive solution that tries every subarray (the first two loops), then computes their sum (the inner most loop). This algorithm can be improved to O(N^2). Here is the code from the lecture.

def max_sum_subarray_better(xs: list[int]) -> int:
    best = 0
    for lwr in range(len(xs)):
        total = 0
        # Incrementally grow subarray
        for i in range(lwr, len(xs)):
            total += xs[i]
            best = max(best, total)
    return best

This algorithm only needs two loops. It speeds up the previous algorithm by mainting a running "total" variable to keep track of the sum of the current subarray. It updates this total as the size of the subarray considered increases. This means it does not need a third loop. It is O(N^2) since the two loops look at all n*(n+1)/2 (which is O(n^2)) pairs of (lwr, i). For the purposes of complexity analysis, it is useful to know that there are n*(n+1)/2 non-empty subarrays for an array of length n, as this analysis comes up often in algorithms. This is related to the formula for n choose 2. Recall (see here for more info) that n choose 2 = n*(n-1)/2 is the number of ways of choosing 2 elements from a set of elements where the order does not matter. Informally, if you have n different coloured cubes, then n choose 2 is the number of ways to select a pair of cubes that are both different colours, and we don't care about the order so that (red, blue) is a duplicate of (blue, red). The number of subarrays is n choose 2 + n = n*(n-1)/2 + n = n*(n+1)/2. The "+ n" part counts all the subarrays of length 1.

Go to the DOMjudge server (http://domjudge.gozz.au/) and log in. Select "lab2" from the menu at the top right. Let's try using the O(N^3) algorithm. Open the "maxsumsubarraysmall" problem and write a solution using the max_sum_subarray_naive function above. If you submit this solution, you should get a TIMELIMIT verdict. This makes sense, since in the problem N can be up to 2000. Using some rough analysis, we expect the O(N^3) algorithm to do (very roughly) 2000^3=8000000000 operations, and we know that we can do about 10^8 Python operations per second giving us a very rough estimate of the runtime at 80 seconds. Since the time limit is 2 seconds (see the Problemset page on DOMjudge) we don't expect it to pass.

The O(N^2) algorithm we do expect to pass. Try doing a similar very rough estimate of runtime to see why. Create a new solution based on the max_sum_subarray_better function and submit it. Make sure you submit to the "maxsumsubarraysmall" problem. This should get a CORRECT verdict if you implemented your program correctly.

## A Faster Algorithm using Divide and Conquer
In the lectures we have seen several Divide and Conquer algorithm. These include merge sort and quicksort. The "Divide and Conquer" strategy is an algorithmic problem solving paradigm. It refers to a general type of algorithm that recursively breaks down a problem into smaller subproblems (divide), solves those subproblems (conquer), and then combines the answers together to get a final result. A good way of thinking about divide and conquer algorithms is that they have three stages. Stage 1 is to divide the problem into smaller subproblems. Stage 2 is to recursively solve those subproblems. Stage 3 is to combine the answers to those subproblems.

Consider merge sort. It divides an array into two even halves. This is Stage 1. It then recursively sorts the two halves, this is Stage 2. Finally, it merges the two sorted halves together. This is Stage 3.

Now, consider quicksort. It partitions the array so that all the elements less than the partition come before it, and all other elements come after this. This is Stage 1, since it divides the array. Next, quicksort recursively sorts the two sides of the partition, this is Stage 2. Finally, quicksort simply returns the result--it has a trivial Stage 3.

From this viewpoint, we can see that merge sort and quicksort are both divide and conquer algorithms. Merge sort has a more complicated Stage 3 in which it merges, and quicksort has a more complicated Stage 1 where it partitions. However, they both follow the same general problem solving paradigm.

The final part of this lab is to come up with a divide and conquer algorithm to solve the maximum sum subarray problem. Our target worst-case time complexity is O(N log N), similar to merge sort. Please look at the "maxsumsubarraylarge" problem on DOMjudge. Try submitting your O(N^2) and O(N^3) programs to this problem. Both should get TIMELIMIT, which makes sense given that N is now up to 200,000. Repeat the very rough estimate from before with N=200,000 to see why O(N^2) is not expected to pass but O(N log N) is. Try to come up with an O(N log N) divide and conquer algorithm. Following is a series of hints to guide you. Please look at these hints in sequence if you need them, but try to solve the problem using as few hints as possible (within a reasonable timeframe).

Hint 1: Think about the divide and conquer strategy, what is your Stage 1, 2, and 3? Also, since your solution should be recursive, start by thinking about what the base case is. In particular, what should your recursive function return when the length of the subarray is 1?
Hint 1.5: The base case is a subarray of size 1. It should return either 0 or the value of the single element in that subarray.
Hint 2: You can use merge sort as a template. Try to use a similar Stage 1 that divides the array into same-sized halves.
Hint 3: Stage 2 is straightforward. Recursively find the maximum sum subarrays in either half. Stage 3 may seem straightforward--just take the maximum of the solutions to either half. However, it is more complicated than it seems. Can you see what is missing?
Hint 4: For Stage 3, you need to find the maximum sum subarray that crosses the midpoint. This can be done by finding the maximum sum subarray that goes left from the midpoint, and the maximum that goes right from the midpoint. Then, combining these by taking their sum. To combine everything together, take the maximum of the midpoint crossing solution, the solution to the left half, and the solution to the right half.

### Bonus Question:

It is possible to solve the maximum sum subarray problem in O(N). Can you see a way?

Hint 1: Consider subarrays starting from the first element. As they grow, at some point we may need to discard the first element. When would this happen?
Hint 2: A subarray is a prefix with another, smaller prefix removed. For a given prefix, what is the best prefix to remove to maximize the subarray sum?
Hint 3: If you are still stuck, have a look at the Wikipedia page for Maximum Sum Subarray, which talks about this history of the problem and gives the classic solution. Make sure you understand the solution and how it relates to the previous hints.