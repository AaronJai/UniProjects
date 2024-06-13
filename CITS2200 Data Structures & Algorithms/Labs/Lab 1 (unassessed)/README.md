# CITS2200 Exercise 1: Sorting and Searching

Implement all the function stubs in `sorting.py` and `searching.py`.

You are encouraged to write your own tests, and to compare your implementations with other students and attempt to break each other's implementations.

Remember the objective is for you to understand the logic behind these algorithms.
It is not sufficient to simply end up with working code, or be able to explain the algorithms step by step.
Your understanding should be sufficient that you can apply these logical ideas to novel problems in the future.

You should be able to write a logical argument for the correctness and time complexity of each algorithm.
Practise doing so, and see if other students and lab facilitators find your arguments convincing.
You argument should be sufficient to convince a fellow student who has never seen this algorithm before of its correctness.

Consider the following questions.
You are encouraged to discuss them with other students:
1. Are there any scenarios in which insertion sort would be faster than merge sort?
    
    insertion sort time complexity O(n^2), merge sort time complexity O(n logn)
    insertion sort's best case approaches O(n) while merge sort stays constant.
    meaning that insertion sort is better for scenarios where the data is all nearly sorted.

    Also, insertion sort's space complexity is O(1) while merge sort is O(n), insertion sort also better at 'smaller' input sizes.


2. If you need to find a single element in a list, is it worth sorting then binary searching? How many elements would we need to be searching for to make it worth it?
    
    simply looping through to find a single element can take O(n)
    to do binary search, you would definitely need to look at sorting first, but the time complexity will be O(logn)
    so, binary search will be beneficial for large datasets.

3. How might you find the smallest 100 elements of a large unsorted list?

    like above, you can loop but it can take O(n) so if its a really large list use binary search which is O(logn).

4. Could you use binary search to find the turning point of a parabola? How?
    
    get derivative of x, binary search to find where x = 0.

    
