# CITS2200 Exercise 2: ArrayList and HashMap

Python is a very high level language, to the point that it doesn't even provide you more fundamental data structures like fixed-size arrays.
Instead the basic built-in data structures of Python include `list` and `dict`, which are implementations of dynamically-sized arrays and hash maps, respectively.
Obviously, we do not wish for you to use these data structures regularly without understanding them, so in this exercise we will be implementing basic versions of each.

Implement a dynamically-sized list by implementing all the function stubs in `arraylist.py`.
While your implementation will probably require a Python `list`, in order to model a fixed-size array you are not allowed to use any list operations that would cause a list to change size.
Once you have created a list, it must remain the same length at all times.
You may, however, construct a new list of a different size and discard the old one.

Implement a hash map by implementing all the function subts in `hashmap.py`.
It should be obvious that your implementation may not use a Python `dict`.

Complexity targets for some methods are included in their doc comments.

Sample tests are provided in `test_arraylist.py` and `test_hashmap.py` and can be invoked with `python -m unittest` in this directory.
You are encouraged to write your own additional tests, and to compare your implementations with other students and attempt to break each other's implementations.

Remember the objective is for you to understand the logic behind these algorithms.
It is not sufficient to simply end up with working code, or be able to explain the algorithms step by step.
Your understanding should be sufficient that you can apply these logical ideas to novel problems in the future.

You should be able to write a logical argument for the correctness and time complexity of each algorithm.
Practise doing so, and see if other students and lab facilitators find your arguments convincing.
You argument should be sufficient to convince a fellow student who has never seen this algorithm before of its correctness.

Consider the following questions.
You are encouraged to discuss them with other students:
1. What is the worst-case complexity of your `HashMap` operations?
2. If we wish to recover memory as we remove elements from our data structures, how much should we shrink them by, and when? How does this affect amortization?
3. What `ArrayList` operations could be done faster with a linked list? Can you think of a scenario in which a linked list is the better choice?
