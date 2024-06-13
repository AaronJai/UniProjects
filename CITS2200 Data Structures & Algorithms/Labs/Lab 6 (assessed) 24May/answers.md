# CITS2200 Lab 6: Tranes and Planes, Security Routing

Name: AARON TAN ZHENG JIE

Student Number: 22884212


## Question 1 (3 marks)
Implement your solution by filling out the method stub in `trains_planes.py`.
Your implementation must pass the tests given in `test_trains_planes.py`, which can be invoked by running `python -m unittest test_trains_planes`.

See `trains_planes.py`.


## Question 2 (1 mark)
Give an argument for the correctness of your `trains_planes()` function.

YOUR ANSWER HERE
    The task asks us to determine which flights can be replaced by trains based on the development of new rail connections over time.
The data structure I researched and implemented was a union-find which is good in this scenario since it can efficiently manage which cities are
connected as new train routes are added.Every time a new train route is given, the union-find structure merges the groups of connected cities, 
updating the overall connectivity.
    When we're trying to see if a flight can be replaced, the function chekcs if the departure and arrival cities belong to the same group in
the union find - done using the find() method.
    If both cities are in the same group, they are connected by trains (directly or indirectly via other cities) and so tells us if the flight
can be replaced by a train.
    It's also good in that it guarantees all train connections up to the date of each flight are considered so we don't do any misidentification
of flights that can be replaced but actually can't.


## Question 3 (1 mark)
Give an argument for the complexity of your `trains_planes()` function.

YOUR ANSWER HERE
    Our complexity can be considered the target O(N log N) where N represents the total number of train and plane entries combined. what contributes to
this is the sorting of lists of trains & planes, and operations that we perform in the union-find data structure.
1. first we sort the list of trains and planes based on dates. - this has complexity O(T log T) and O(P log P) for trains and planes respectively.
    and in complexity when summing occurs like this the overall step will just be O(N log N)
2. the operations in union-find are almost constant time using something to do with path compression and union by rank. And if they are close to constant,
    the intial sorting step from before will dominate.
3. During the processing of trains and plance, each entry in the sorted list triggers a union operation (for trains) or a find operation (for planes). Since
    each operation is nearly constant time, and every entry is processed once, this leads to a linear time O(N)

So, given all the complexities, it is all dominated by the first step O(N log N)

## Question 1 (3 marks)
Implement your solution by filling out the method stub in `security_routing.py`.
Your implementation must pass the tests given in `test_security_routing.py`, which can be invoked by running `python -m unittest test_security_routing`.

See `security_routing.py`.


## Question 2 (1 mark)
Give an argument for the correctness of your `security_route()` function.

YOUR ANSWER HERE
    Our task is to find the fastest route from a source station to a target station but with a twist that is the security clearances.
Though mentioned but not explored much in our lecture, I looked a bit into Dijkstra's algorithm, which is a well known algorithm for finding
shortest paths in a graph. This is what we did:
1. we consider both station location and the current security clearance as part of the node's state,
2. We use a priority queue to process the least costly path first and expands paths in order of increasing travel time.
3. when a station is visited, we have a function to check if we can update the security clearance based on the station's capabilities
    (allows function to adapt to new clearances that might allow faster routes)
4. function then checks outgoing segments from the station, and if the segment's security requirements are met with the current clearance,
    it updates the path to the next station.
5. if target station is reached, return shortest time (but also important to verify its a valid path)

## Question 3 (1 mark)
Give an argument for the complexity of your `security_route()` function.

YOUR ANSWER HERE
    The function uses a priority queue to handle each station and any possible security clearances which lead to operations depending
on both the number of stations and segments.
    For each segment, the function checks multiple possible clearances which can increase the number of operations.
    The main operations (adding and removing from our queue) happen in logarithmic time relative to potential station-clearance
combinations. 
    So, our total complexity would be O(S log M) where S is the number of segments (the processing of them) and M is the number of stations
(from managing the priority queue).
    In some cases then, this would reach the target complexity O(N log N) but this would depend on the specific relationship between
segments and stations, e.g., in dense graphs where segments outnumber stations thus in that case it can exceed it.