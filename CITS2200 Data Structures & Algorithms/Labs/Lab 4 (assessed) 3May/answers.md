# CITS2200 Lab 2: Genealogy

Name: AARON TAN

Student Number: 22884212


## Question 1 (1 mark)
Write a simple description of how you are going to represent the problem as a data structure.
Your description should justify how the representation is going to help you solve the problem within the target complexities.

YOUR ANSWER HERE
Task: 1. determine who should be Envoy and 2. determine how closely related two Kiktil are.
The primary data structure I believe is best here is through a dictionary to represent the relationships within the genealogy.
We can use the DICTIONARY to map parent names to a lists of their child names.

Using a dictionary also helps as they are implemented using hash tables which allow for a more consistent time complexity O(1) for look-ups, 
which is important since we'd need to frequently check whether a parent already exists in the structure before appending any children for example.

In hindsight I definitely could've looked into implementing a tree structure since at first it would seem to more
naturally represent hiearchical structure like this geneology. I recognise both trees and dicts can be used especially to attain the 
targets of the lab but honestly went with dicts also because I was more comfortable working with them here, and seemed to be efficient enough
for the given tasks it needed to complete.

## Question 2 (1 mark)
Write a simple description of the algorithm you have designed for `get_cousin_dist()`.
Your description should justify the correctness of your algorithm, and make an argument as to its time complexity.

YOUR ANSWER HERE
Task: find the degree of cousins (maxmimum number of generations below the most recent common ancestor (MRCA)), and removal (difference in
generations between two cousins from the MRCA)

Design:
1. reverse the dictionary process here to instead make the child a key, and parent the value. This makes it a lot easier to then find the MRCA since
    we can see the list of parents for a child, and see where they diverge when compared to another child.
2. trace_lineage() function we defined generates a lineage for a Kitkil, from the originator down to them. This is built by tracing the parents
using the parent_map and reversed to order it downwards.
3. we can then use this function on lhs_name and rhs_name
4. calculations done here: 
    order = subtracting the index of the MRCA from total elngth of the lineage - 1.
    Degree = maximum of the two orders (use max function)
    Removal = absolute difference between the two orders (use abs function)

    Building the parent map is O(N) since each individual is processed at least once to the dictionary.
    our trace_lineage() function is O(h) where h is the maximum depth of the kiktil to the originator and in the worst case could be close to N
    ONLY for unbalanced trees. though it could be an issue, I researched that in secnarios like this h is typically much less than N.
    The calculations at the end is O(1) so it can be ignored.
    So overall, the safe estimate would be like the target complexity O(N)..


## Question 3 (5 marks)
Implement your design by filling out the method stubs in the `Genealogy` class found in `genealogy.py`.
You are **not** allowed to import any modules.
Your implementation must pass the tests given in `test_genealogy.py`, which can be invoked by running `python -m unittest`.

See `genealogy.py`.


## Question 4 (1 mark)
Give an argument for the correctness and complexity of your `get_primogeniture_order()` function.

YOUR ANSWER HERE
Task: get the child of the originator then grand-children if any, before moving onto any more children of the originator if any.
Implementation: I found it easy to use a recursive depth-first search function (like a stack).
    - This method starts with the originator and recursively visits each of its children before moving to the next sibling, ensuring that 
    the entire lineage of the eldest child is explored before any younger siblings, and so forth.

Visualisation:
    Suppose we have 
        Alice                          
        ├── Bob
        │   ├── Ella
        │   └── Frank
        ├── Charlie
        │   └── George
        └── Dana

    1.Start DFS with Alice:
    DFS Call: dfs("Alice")
    Action: Add "Alice" to order.
    State: order = ["Alice"]
    Next: Call dfs("Bob") - Alice's eldest child.
    
    2.DFS on Bob:
    DFS Call: dfs("Bob")
    Action: Add "Bob" to order.
    State: Order = ["Alice", "Bob"]
    Next: Call dfs("Ella") (Bob's eldest child).
    
    3.DFS on Ella:
    DFS Call: dfs("Ella")
    Action: Add "Ella" to order.
    State: order = ["Alice", "Bob", "Ella"]
    Next: Since Ella has no children, return and call dfs("Frank").
    
    4.DFS on Frank:
    DFS Call: dfs("Frank")
    Action: Add "Frank" to order.
    State: order = ["Alice", "Bob", "Ella", "Frank"]
    Next: Since Frank has no children, return and do Bob's children, then return to Alice and call dfs("Charlie").
    ...

Complexity: The traversal visits each Kiktil exactly once (linearly) so it hits the target complexity O(N), aided by the
dictioanry's O(1) access time for traversal/retrieval.


## Question 5 (1 mark)
Give an argument for the correctness and complexity of your `get_seniority_order()` function.

YOUR ANSWER HERE
Summary:
Originator's children are one generation, their children are the next
Within each generation, individuals are ordered from eldest to youngest.
Cousins are prioritized based on their ancestral order in the previous generation. This means if two cousins are in the same generation, 
their order is based on the relative seniority of their parents.

Implementation: My thought here is to implement a breadth-first search approach (using a queue) 
    - makes sure we visit one depth (generation) before going to the next depth.
    - All nodes (children) are added to [the end] and removed from [the front of] the queue in FIFO order

Visualisation:
    Suppose we have an Originator with two children, A and B. A and B each have two children, making a third generation.
Start: Queue = [Originator]
First Iteration: Dequeue Originator, Enqueue A and B → Queue = [A, B]
Second Iteration: Dequeue A, Enqueue A's children → Queue = [B, A1, A2]
Third Iteration: Dequeue B, Enqueue B's children → Queue = [A1, A2, B1, B2]
Next : Continue processing A1, A2, then B1, B2.

Complexity: And likewise, since we are visiting each Kiktil once and in linear fashion, it hits target complexity O(N)
list.pop(0) could lead to O(N) also due to list re-indexing, but overall its still O(N) since each element is enqueued and dequed exactly once.
Initially i thought complexity could be affected using extend() given the note about the insert() method but found that extend() which adds multiple 
elements to the end of the list typically operates in amortised O(1) time per element added.


## Question 6 (1 mark)
Give a brief explanation of the function and purpose of any data structures you implemented.

YOUR ANSWER HERE
This should be partly answered in previous questions but to reiterate key points:

our primary data structure used is a dictionary which maps a parent (key) to a list of children (value), and each child
can also be a key as they would have their own children and so forth.
Dictionaries also allow for better robustness and maintainability since it can allow for dynamic modifications of the genealogy
without restructuring the entire data.
Not only is this the most efficient way to store the data but it allows for constant time complexity O(1) when we need to access
a kiktil's list of children.

In our get_seniority_order() function, the list used as a queue to manage the BFS process
- indivudals enqueued and dequeued in FIFO form. - see explanation/visualisation in Q5.
- this is the best way in the context of this function since we want to process everyone in a single generation before moving to the next.

________________________________________________________________________________________________________________________________________________________________
Not that its really implementing anything more but:
in get_primogeniture_order() it utilises our primary dict structure and navigates the tree in a depth-first manner.
    - though we aren't implementing a new data structure, the recursion aspect of dfs() relies on the CALL STACK (managed by the programming
    language's runtime)
    - Each recursive call to explore a node (person/kiktil) and their descendants pushes a frame onto the call stack, and popping these frames as the 
    function returns from calls mimics the behavior of explicitly using a stack

in get_cousin_dict() we also use a dictionary, though reversed (children are key, parent are values) to help find and compare where the last common ancestor is
    - explanation of how a dict here is good should have been repeated enough.