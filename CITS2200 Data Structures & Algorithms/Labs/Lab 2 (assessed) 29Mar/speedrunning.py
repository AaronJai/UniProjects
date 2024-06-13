# Name: AARON TAN
# Student Number: 22884212
# (Answers at end)

class Leaderboard:
    def __init__(self, runs=[]):
        # Initialise leaderboard with runs provided
        self.runs = []
        for time, name in runs: 
            self.submit_run(time, name)

    def get_runs(self):
        return self.runs

    def submit_run(self, time, name):
        # Insert run in sorted manner
        
        insert_index = 0
        for index, (existing_time, _) in enumerate(self.runs): # used '_' as placeholder for name; readability purposes.
            # Check if the current run time is less than the existing time
            if time < existing_time:
                break
            # If times are equal, compare names alphabetically
            elif time == existing_time and name < self.runs[index][1]:
                break
            insert_index += 1
        # Insert the new run at the correct position
        self.runs.insert(insert_index, (time, name))

    def get_rank_time(self, rank):
        if rank <= len(self.runs):
            return self.runs[rank - 1][0] # Return time of run at given rank
        else:
            return None # If rank given more than number of runs. Changed from '-1' after Amitava's email.

    def get_possible_rank(self, time):
        # Find rank based on possible time
        
        left, right = 0, len(self.runs)
    
        while left < right:
            mid = (left + right) // 2
            if self.runs[mid][0] < time:
                left = mid + 1
            else:
                right = mid

        return left + 1 # to account for indexing

    def count_time(self, time):
        # Count the number of runs with the given time using binary search.
        def find_first():
            left, right = 0, len(self.runs)
            while left < right:
                mid = (left + right) // 2
                if self.runs[mid][0] < time: 
                    left = mid + 1 # target must be in right half
                else:
                    right = mid
            return left

        def find_last():
            left, right = 0, len(self.runs)
            while left < right:
                mid = (left + right) // 2
                if self.runs[mid][0] <= time: # '<=' continues search to the right
                    left = mid + 1
                else:
                    right = mid
            return left - 1 # loop exit points to position after the last occurence of 'time' since the loop overshoots by 1

        first_index = find_first()
        last_index = find_last()

        # Ensure that the time is actually present in the runs - indices are valid, within range, and correctly point to entries in the list that match the specified time
        if first_index <= last_index and 0 <= first_index < len(self.runs) and self.runs[first_index][0] == time:
            return last_index - first_index + 1 # since count is inclusive. E.g., indices 3 and 5 is 3, 4, 5 (5-3+1, not 5-3)
        return 0
    

"""
**Question 1 (1 mark):**
Write a short paragraph explaining the relationship between this problem and more abstract computer science topics we have covered in class.
---

Some computer science topics we covered were searching and sorting algorithms.
This problem involves a storing data that also needs to be sorted. Depending on the amount of data that this program may potentially use we can explore ways
in which we can sort out data including sorting algorithms such as insertion sort and merge sort to make it more efficient.
Realistically though, efficiency would be better for large datasets. At small datasets, real-time operation of algorithms like insertion sort and 
merge sort despite its different worst-case complexity is negligible/hard to differentiate with testing. That said, for the type of 'small datasets' that reach maybe
up to 1000 points of data, we can explore insertion sort.

Given that the program also incorporates getter methods to return some value, it may prove useful to see how we can utilise binary search to make our 
program more efficient for large datasets rather than simply looping through the entire dataset.


**Question 2 (1 mark):**
What data do you need to store in the `Leaderboard` class?
What algorithm do you intend to use for each method?
---

- The 'Leaderboard' class stores a list of runs containing time, name tuple pairs.

- Originally, I was looking to incorporate insertion sort for how we sort the data/data being added. However I discovered that we may not necessarily need 
either insertion or merge sort here. In submit_run(), iterating over the 'runs' list takes O(n) time, and within the loop the simple operations like comparisons 
are made between the given run time and existing run times, and between names if the times are equal which take O(1). Lastly, inserting the new run at the correct 
position takes O(n) in worst case if it's at the end of the list. i.e., the overall complexity here is O(n).
Finally since the __init__() method calls submit_runs() within a for loop, the total complexity is O(n^2), which is the same as insertion sort. and it sorts all our data.
Original instructions said in __init__() that "The given list of runs is not required to be in order." but it made the most sense to me to do it the way I did. If a user simply
initialised with their set of runs without being in order we need to find a way to sort it still and it made less sense to create a sorting method to be used in submit_runs() when
all it is doing is as it says, to submit a new time and name pair. If we used a sorting method like merge sort it'll change submit_runs() itself from O(n) to O(logn) and insertion sort
from O(n) to O(n^2). If we then include __init__() calling submit_runs() the whole program becomes more inefficient utilising either of the sorting algorithms.


- get_runs() doesn't need an algorithm, just returning the list.

- get_rank_time() I initially thought maybe binary search since it's a getter, but realised it doesn't need it because the list is sorted and we're actually 
just directly accessing the element at the rank index so it's O(1)

- get_possible_rank() more suited for binary search since unlike above we arent accessing an index and are searching based on a target.

- Originally had a loop for count_time() and a counter variable, but realised we can also use binary search. what we can do is use binary search to find the first 
and last occurence of the given time and subtract the two allowing us to have a O(logn) complexity instead of O(n).


**Question 4 (1 mark):**
Give an argument for the correctness and complexity of your `__init__()` function.
---
The correctness of the __init__ function in the Leaderboard class stems from its reliance on the submit_run method to insert initial runs into an empty list in a sorted order. 
Though not required, this design choice ensures that the leaderboard is correctly sorted from the moment it is instantiated, which is critical for all future operations assuming the list is sorted. 
Since submit_run handles each insertion with respect to the leaderboard's ordering rules (time and then name), using it during initialization abstracts away the complexities of sorting algorithms such
as insertion sort and merge sort, simplifying the design. 

Regarding complexity, inserting each run individually with submit_run implies that for every run added, the method potentially scans the entire list to find the correct insertion point. This results in a 
time complexity that grows quadratically with the number of initial runs, O(n^2), because for each of n insertions, the cost is proportional to the size of the list, which grows linearly with the number of 
runs already inserted.


**Question 5 (1 mark):**
Give an argument for the correctness and complexity of your `submit_run()` function.
---
submit_run() is designed to maintain the sorted order of the leaderboard by inserting a new run at the correct position according to its time and, if necessary, its name. The method iterates over the existing 
runs, comparing times and names to determine the precise location for the new run. This ensures that the leaderboard always reflects the correct ranking order after each submission. 
As a result, the complexity of submit_run() is O(n), which, in the context of dynamic, continually updated data structures like a leaderboard is more efficient that incorporating other sorting algorthims.

Without going into too much detail, here is a rough explanation of why we don't need to consider the other algorithms using its already known complexities:
Insertion Sort: If each new run triggered a sort of the entire leaderboard using insertion sort, while the sort itself would have an average and worst-case complexity of O(n^2) since it has to iterate over the entire list,
and then compare that element to the one before (like a nested loop). If then you combine this with __init__(), complexity will then approach O(n^3)
Merge Sort: Although merge sort has a average and worst-case complexity of O(nlogn), since it has to halve the list until one element remains, and then merge them together. Again when combining with __init__(), 
complexity reaches O(n^2 logn)


**Question 6 (1 mark):**
Give an argument for the correctness and complexity of your `count_time()` function.
---
It is possible to simply loop through the entire list, n, and increment the counter variable for the desired time which gives us O(n), but we are looking for efficiency. Though it may appear more complicated we can
utilise two binary search operations - one to find the first occurence of the number, another to find the last. Subtract the two and we get our count.

Each binary search operation has a time complexity of O(logn), where n is the number of elements in the list. This is because, when we apply binary search, we're leveraging a fundamental property: if you're looking 
for a specific value in a sorted sequence, any deviation to the left or right inherently narrows down the search space to the segment where the value must reside if it exists at all. Thus, the size of the 
search space is halved in each step, leading to a logarithmic time complexity.

Finding the First Occurrence
When looking for the first occurrence of a time, we don't want to skip over it by moving too far to the right. The condition if self.runs[mid][0] < time: helps us achieve this by narrowing down the search space.

Finding the Last Occurrence
For the last occurrence, the condition if self.runs[mid][0] <= time: adjusts our approach slightly to ensure we capture the last instance of the target time:
When the time at the current midpoint is equal to the target time, we can't be certain this is the last occurrence. There could be more instances to the right. So, unlike when searching for the first occurrence,
we now include the current midpoint in our search space and move right to ensure we're not missing out on later occurrences.

Although we are conducting two binary search operations, they are sequential and not nested. When you perform two sequential operations each with a complexity of O(logn),
the overall complexity is O(logn) + O(logn) which simplifies to O(logn). This is because, in asymptotic analysis, we are interested in the dominant term that grows the 
fastest as the input size increases. Constant factors and lower-order terms are not considered. After finding the indices of the first and last occurrences, we subtract 
them to find the count. This subtraction is a constant-time operation, O(1), and does not affect the overall time complexity of the algorithm. The dominant factor is still 
the binary search operations.


"""