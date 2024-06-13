# Name: AARON TAN
# Student Number: 22884212

class Genealogy:
    """The genealogy and succession order for Envoy of the Kiktil."""

    def __init__(self, originator_name):
        """Constructs an initial genealogy containing no individuals other than
        the Originator.

        Args:
            originator_name: The name of the Originator of the Kiktil species.
        """
        self.originator = originator_name
        self.family = {originator_name: []} # Dictionary to store child relationship


    def add_child(self, parent_name, child_name):
        """Adds a new child belonging to a given parent.

        You may assume the parent has previously been added as the child of
        another individual, and that no individual named `child_name` exists.

        Target Complexity: O(1) expected.

        Args:
            parent_name: The name of the parent individual.
            child_name: The name of their new child.
        """
        if parent_name in self.family: # check if parent exists
            self.family[parent_name].append(child_name) # if parent exists, append child
            self.family[child_name] = [] # initialise each child to be able to have their own children
        pass

    def get_primogeniture_order(self):
        """Returns the primogeniture succession order for Envoy of the Kiktil.

        By primogeniture, succession flows from parent to eldest child, only
        moving to the next youngest sibling after all their elder sibling's
        descendants.

        Target Complexity: O(N), where N is how many indivduals have been added.

        Returns:
            A list of the names of individuals in primogeniture succession order
            starting with the Originator.
        """
        order = []

        # Implementing a depth-first search approach
        def dfs(person): 
            order.append(person)
            
            for child in self.family[person]:
                dfs(child)
        
        dfs(self.originator)
        return order

    def get_seniority_order(self):
        """Returns the seniority succession order for Envoy of the Kiktil.

        Seniority order prioritizes proximity to the Originator, only moving on
        to a younger generation after every individual in the previous
        generations. Within a generation, older siblings come before younger,
        and cousins are prioritized by oldest different ancestor.

        Target Complexity: O(N), where N is how many indivduals have been added.

        Returns:
            A list of the names of individuals in seniority succession order
            starting with the Originator.
        """
        order = []
        queue = [self.originator]  # Start with the Originator
        
        while queue:
            current = queue.pop(0)  # Get the first person in the queue
            order.append(current)   # Add them to the order
            # Enqueue all children of the current person, which are already sorted by age
            queue.extend(self.family[current])
        
        return order
        

    def get_cousin_dist(self, lhs_name, rhs_name):
        """Determine the degree and removal of two cousins.

        The order of an individual relative to an ancestor is the number of
        generations separating them. So a child is order 0, a grandchild is
        order 1, and so on.
        Consider the orders of two individuals relative to their most recent
        shared ancestor.
        The degree of the cousin relation of these individuals is the greater of
        their orders.
        The removal of the cousin relation is the difference in their orders.

        Target Complexity: O(N), where N is how many indivduals have been added.

        Args:
            lhs_name: The name of one cousin.
            rhs_name: The name of the other cousin.

        Returns:
            A pair `(degree, removal)` of the degree and removal of the cousin
            relation between the specified individuals.
        """
        # p1: Build the parent map
        parent_map = {}
        for parent, children in self.family.items():
            for child in children:
                parent_map[child] = parent

        # Helper function to trace lineage back to the originator
        def trace_lineage(person):
            lineage = []
            while person in parent_map:
                lineage.append(person)
                person = parent_map[person]
            lineage.append(person)  # Append the originator or the starting person
            return lineage[::-1]  # Reverse to start from the originator to the person

        # p2: Trace lineage for both individuals 
        lhs_lineage = trace_lineage(lhs_name)
        rhs_lineage = trace_lineage(rhs_name)

        # p3: Find MRCA by tracing the lineages from the originator
        index = 0 # initialise index
        min_length = min(len(lhs_lineage), len(rhs_lineage)) # limits to length of the shorter lineage, no point looking any longer.

        # iterate as long as index within range, and is still a common ancestor (until they diverge)
        while index < min_length and lhs_lineage[index] == rhs_lineage[index]:
            index += 1

        # Calculate the orders relative to the MRCA, subtract 1 to account for indexing
        lhs_order = len(lhs_lineage) - index - 1
        rhs_order = len(rhs_lineage) - index - 1

        # p4: Calculate degree and removal
        degree = max(lhs_order, rhs_order)
        removal = abs(lhs_order - rhs_order)

        return (degree, removal)
    

