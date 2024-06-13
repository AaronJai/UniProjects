# Name: AARON TAN ZHENG JIE
# Student Number: 22884212


def trains_planes(trains, planes):
    """Find what flights can be replaced with a rail journey.

    Initially, there are no rail connections between cities. As rail connections
    become available, we are interested in knowing what flights can be replaced
    by a rail journey, no matter how indirect the route. All rail connections
    are bidirectional.

    Target Complexity: O(N lg N) in the size of the input (trains + planes).

    Args:
        trains: A list of `(date, lcity, rcity)` tuples specifying that a rail
            connection between `lcity` and `rcity` became available on `date`.
        planes: A list of `(code, date, depart, arrive)` tuples specifying that
            there is a flight scheduled from `depart` to `arrive` on `date` with
            flight number `code`.

    Returns:
        A list of flights that could be replaced by a train journey.
    """
    class UnionFind:
        def __init__(self):
            self.parent = {} # Dict to store parent of each item
            self.rank = {}  # Dict to store rank of each item (used in union by rank later)

        def find(self, item):
            # Makes the tree flatter by setting the parent of each node on the path directly to the root.
            if self.parent[item] != item:
                self.parent[item] = self.find(self.parent[item])
            return self.parent[item]

        def union(self, set1, set2):
            # Find the roots of the sets in which elements set1 and set2 are.
            root1 = self.find(set1)
            root2 = self.find(set2)
            # If they are in different sets, union them.
            if root1 != root2:
                # attach the smaller tree under the root of the larger tree.
                if self.rank[root1] > self.rank[root2]:
                    self.parent[root2] = root1
                elif self.rank[root1] < self.rank[root2]:
                    self.parent[root1] = root2
                else:
                    # If ranks are the same, make one root of the other and increase the rank.
                    self.parent[root2] = root1
                    self.rank[root1] += 1

        def add(self, item):
             # Add a new item to the union-find structure if it is not already present.
            if item not in self.parent:
                self.parent[item] = item
                self.rank[item] = 0

    uf = UnionFind() # Initialize the union-find instance.

    # Initialize union-find structure with all cities mentioned in trains
    for _, lcity, rcity in trains:
        uf.add(lcity)
        uf.add(rcity)

    # Sort trains and planes by date
    trains.sort(key=lambda x: x[0])
    planes.sort(key=lambda x: x[1])

    # Process train connections
    train_index = 0 # Index to keep track of which train connection is to be processed next.
    n_trains = len(trains) # Total number of train connections.

    replacable_flights = [] # List to store flights that can be replaced by train journeys
    for flight in planes:
        code, fdate, depart, arrive = flight

        # Process all train connections up to the date of the flight
        while train_index < n_trains and trains[train_index][0] <= fdate:
            _, lcity, rcity = trains[train_index]
            uf.union(lcity, rcity) # Connect the cities by train in the union-find structure.
            train_index += 1

        # Check if the flight can be replaced by a train
        if uf.find(depart) == uf.find(arrive):
            replacable_flights.append(flight) # If can replace, add the flight to the list of replaceable flights.

    return replacable_flights
