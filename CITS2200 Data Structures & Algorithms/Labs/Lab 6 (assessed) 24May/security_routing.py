# Name: AARON TAN ZHENG JIE
# Student Number: 22884212

from enum import IntEnum

# import python built in modules
import heapq
from collections import defaultdict, deque


class Clearance(IntEnum):
    NONE = 0
    RED = 1
    BLUE = 2
    GREEN = 3


def security_route(stations, segments, source, target):
    """Finds the fastest route from source station to target station.

    You start with no security clearance.
    When at a security station, you may choose to set your clearance to the same
    as that of the station.
    Each segment gives how long it takes to get from one station to another, and
    what clearance is required to be able to take that segment.

    Target Complexity: O(N lg N) in the size of the input (stations + segments).

    Args:
        stations: A list of what clearance is available at each station, or
            `NONE` if that station can not grant any clearance.
        segments: A list of `(u, v, t, c)` tuples, each representing a segment
            from `stations[u]` to `stations[v]` taking time `t` and requiring
            clearance `c` (`c` may be `NONE` if no clearance is required).
        source: The index of the station from which we start.
        target: The index of the station we are trying to reach.

    Returns:
        The minimum length of time required to get from `source` to `target`, or
        `None` if no route exists.
    """
    # Create a graph where each node has edges considering clearance requirements
    adj_list = defaultdict(list)
    for u, v, t, c in segments:
        adj_list[u].append((v, t, c))
    
    # Priority queue for Dijkstra's: stores tuples of (time, current_station, current_clearance)
    pq = [(0, source, Clearance.NONE)]
    
    # Dictionary to store the minimum time to reach each (station, clearance) combination
    best_time = {}
    
    while pq:
        current_time, current_station, current_clearance = heapq.heappop(pq)
        
        # If we reached the target station with a valid path, return the time
        if current_station == target:
            return current_time
        
        # Skip processing if we found a better path to this state already
        if (current_station, current_clearance) in best_time and best_time[(current_station, current_clearance)] <= current_time:
            continue
        
        # Record the best time to this state
        best_time[(current_station, current_clearance)] = current_time
        
        # Try to change clearance at the current station
        station_clearance = stations[current_station]  # Get the clearance level available at the current station.
        if station_clearance != Clearance.NONE and (current_station, station_clearance) not in best_time:
            # If the station offers a clearance and it's not already in best_time for this station and clearance level,
            heapq.heappush(pq, (current_time, current_station, station_clearance))  # push the current station and its clearance to the priority queue with the current time.


        # Explore adjacent nodes
        for next_station, travel_time, required_clearance in adj_list[current_station]:  # Iterate over all connections from the current station.

            if required_clearance == Clearance.NONE or required_clearance == current_clearance:
                # If the segment does not require a clearance or if the required clearance matches the current clearance,
                next_time = current_time + travel_time  # calculate the travel time to the next station.

                if (next_station, current_clearance) not in best_time or best_time[(next_station, current_clearance)] > next_time:
                    # If this next station with the current clearance is not yet visited, or a faster time is found,
                    heapq.heappush(pq, (next_time, next_station, current_clearance))  # push the new time and station with current clearance to the priority queue.

    
    # If no path was found, return None
    return None
