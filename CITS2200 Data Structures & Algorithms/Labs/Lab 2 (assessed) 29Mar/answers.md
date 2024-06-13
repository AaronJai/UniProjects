**Question 1 (1 mark):**
Write a short paragraph explaining the relationship between this problem and more abstract computer science topics we have covered in class.
---

This problem involves a list of data that needs to be sorted. Depending on the amount of data that this program may potentially use we can explore ways in which we can sort out data including algorithms such as insertion sort and merge sort to make it more efficient.
Generally though, efficiency would be more important for large datasets as at small datasets real-time operation of algorithms like insertion sort and merge sort despite its different worst-case complexity is negligible (hard to differentiate).

Given that the program also incorporates getter methods to return some value, it may prove useful to see how we can utilise binary search to make our program more efficient for large datasets rather than simply looping through the entire dataset.


**Question 2 (1 mark):**
What data do you need to store in the `Leaderboard` class?
What algorithm do you intend to use for each method?
---

- The 'Leaderboard' class stores a list of runs containing time, name tuple pairs.

- Originally, I was looking to incorporate insertion sort for how we sort the data/data being added. However I discovered that we may not necessarily need either insertion or merge sort here. In submit_run(), iterating over the 'runs' list takes O(n) time, and within the loop the simple operations like comparisons are made between the given run time and existing run times, and between names if the times are equal which take O(1). Lastly, inserting the new run at the correct position takes O(n) in worst case if it's at the end of the list.
Overall, here the complexity is O(n).
Now, since the __init__() method calls submit_runs() within a for loop, the total complexity is O(n^2), which is the same as insertion sort.

- get_runs() doesn't need an algorithm, just returning the list.

- get_rank_time() I initially thought maybe binary search since it's a getter, but realised it doesn't need it because the list is sorted and we're actually just directly accessing the element at the rank index so it's O(1)

- get_possible_rank() more suited for binary search since unlike above we arent accessing an index and are searching based on a target.

- Originally had a loop for count_time() and a counter variable, but realised we can also use binary search. what we can do is use binary search to find the first and last occurence of the given time and subtract the two allowing us to have a O(logn) complexity instead of O(n).


**Question 4 (1 mark):**
Give an argument for the correctness and complexity of your `__init__()` function.
---
__init__()is designed to initialize a class instance with a list of timed runs. It starts with an empty list and iterates through the provided runs list, inserting each run using the submit_run() method. Since submit_run() is assumed to insert each run correctly in a sorted manner (see explanation next in question), calling it for each run guarantees the leaderboard is sorted upon initialization.
Since we're at the stage of initialisation, the complexity will be O(n^2): first the loop iterates over all elements in worst case (i.e., n) and within each iteration of the loop, submit_run method is called, which has a time complexity of O(n) (see explanation in next question).

**Question 5 (1 mark):**
Give an argument for the correctness and complexity of your `submit_run()` function.
---
submit_run() maintains a sorted list of runs by finding the exact position where a new run should be inserted to keep the list ordered. It iterates over the existing runs, comparing the times (and names, if time is equal) to find the insert index. This ensures that the leaderboard remains sorted after each submission, which is important for retrieving runs if needed. The complexity of this function is O(n), where n is the number of elements in the runs list. This is because, in the worst case, it might need to compare the new run with every existing run before finding the appropriate insert position. The insertion itself is O(1) but since we worry about worst case (and not constants), complexity is O(n).

**Question 6 (1 mark):**
Give an argument for the correctness and complexity of your `count_time()` function.
---
Each binary search operation has a time complexity of O(logn), where n is the number of elements in the list. This is because, with each step of the binary search, the size of the search space is halved, leading to a logarithmic time complexity.
Although we are conducting two binary search operations, they are sequential and not nested. When you perform two sequential operations each with a complexity of O(logn), the overall complexity is O(logn) + O(logn) which simplifies to O(logn). This is because, in asymptotic analysis, we are interested in the dominant term that grows the fastest as the input size increases. Constant factors and lower-order terms are not considered. After finding the indices of the first and last occurrences, we subtract them to find the count. This subtraction is a constant-time operation, O(1), and does not affect the overall time complexity of the algorithm. The dominant factor is still the binary search operations.