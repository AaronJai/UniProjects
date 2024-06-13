class ArrayList:
    """A simple dynamically-sized list.

    Note: Python lists are already dynamically sized, so while implementing this
    class, you may not use any methods that would cause a list or other built-in
    data structure to change size. If you ever need to change the size of a list
    you must instead construct a new list of the desired size and copy across.
    """

    def __init__(self):
        """Constructs an empty ArrayList."""
        self._size = 0
        self._data = [None] * 10 # initialise with capacity of 10
        

    def __len__(self):
        """Returns the number of elements in the ArrayList."""
        return self._size


    def __getitem__(self, index):
        """Returns the item at position `index` in the ArrayList.

        This implements the `xs[i]` notation you will be familiar with from
        lists, but there is no need to support ranges or negative indices.

        Args:
            index: The index of the desired element.

        Returns:
            The element at position `index`.

        Raises:
            IndexError: If the index is out of bounds.
        """
        if index >= self._size or index < 0:
            raise IndexError("Cannot get item, index is out of bounds.")
        return self._data[index]


    def __setitem__(self, index, value):
        """Sets the `index` position element in the ArrayList to be `value`.

        This implements the `xs[i] = x` notation you will be familiar with from
        lists, but there is no need to support ranges or negative indices.

        Args:
            index: The index of the element to modify.
            value: The value to store at the given index.

        Raises:
            IndexError: If the index is out of bounds.
        """
        if index >= self._size or index < 0:
            raise IndexError("Cannot set item, index is out of bounds.")
        self._data[index] = value
        

    def reserve(self, n):
        """Ensure ArrayList has capacity at least `n`.

        Grows the ArrayList if required.

        Args:
            n: The desired capacity.
        """
        if n > len(self._data):
            new_data = [None] * n
            for i in range (self._size):
                new_data[i] = self._data[i]
            self._data = new_data

    def append(self, x):
        """Appends `x` to the ArrayList.

        Target Complexity: O(1) amortized.

        Args:
            x: The value to append.
        """
        if self._size >= len(self._data):
            self.reserve(2 * len(self._data))
            
        self._data[self._size] = x
        self._size += 1


    def extend(self, xs):
        """Extends the ArrayList by appending all the items from ArrayList `xs`.

        Target Complexity: O(len(xs)) amortized.

        Args:
            xs: The ArrayList to be appended.
        """
        if len(xs) + self._size > len(self._data): # Check if current capacity is sufficient
            self.reserve(len(xs) + self._size) # Adjust to ensure enough space

        for i in range(len(xs)):
            self.append(xs[i])

    def pop(self):
        """Removes and returns the last element of the ArrayList.

        Target Complexity: O(1).

        Returns:
            The last element of the ArrayList.

        Raises:
            IndexError: If the ArrayList is empty.
        """
        if self._size == 0:
            raise IndexError("Cannot pop, empty ArrayList")
        
        last_element = self._data[self._size - 1]
        self._data[self._size - 1] = None # clear the slot
        self._size -= 1
        return last_element


    def pop_front(self):
        """Removes and returns the first element of the ArrayList.

        Target Complexity: O(N).

        Returns:
            The first element of the ArrayList

        Raises:
            IndexError: If the ArrayList is empty.
        """
        if self._size == 0:
            raise IndexError("Cannot pop front, empty ArrayList")
        
        first_element = self._data[0]

        for i in range(1, self._size): # Start at 1 since we're moving elements to the left
            self._data[i - 1] = self._data[i]

        self._data[self._size - 1] = None # Clear the last element's spot
        self._size -= 1

        return first_element
