class HashMap:
    """A basic key-value HashMap.

    Note: You may not use a python dictionary at any point in this class.

    You should just use Python's built in `hash()` function for hashing keys.
    """

    def __init__(self):
        """Constructs an empty HashMap.
        More advanced implemenations exist, but here we will simply use a list
        for each bucket. Investigate "open addressing" for smarter strategies.
        """
        self._buckets = 10  # A simple choice for demonstration purposes; this could be adjusted.
        self._data = [[] for _ in range(self._buckets)]  # Initialize each bucket as an empty list.


    def __len__(self):
        """Returns the number of elements in the HashMap."""
        return sum(len(bucket) for bucket in self._data)

    def __getitem__(self, key):
        """Returns the value corresponding to the given key in the HashMap.

        Target Complexity: O(1) expected.

        Args:
            key: The key of the desired value.

        Returns:
            The value associated with `key`.

        Raises:
            KeyError: If the key is not in the HashMap.
        """
        hash_value = hash(key)  # Get the hash value of the key
        bucket_index = hash_value % self._buckets  # Find the appropriate bucket
        bucket = self._data[bucket_index]  # This is the list of items for this bucket
        
        # Search for the key in the bucket
        for kv in bucket: # bucket is the list
            if kv[0] == key:
                return kv[1]  # Return the value associated with the key
        
        # If the key was not found in the bucket, raise KeyError
        raise KeyError("Key not in HashMap")
    

    def __setitem__(self, key, value):
        """Associates `value` with the given `key` in the HashMap.

        Target Complexity: O(1) amortized.

        Any previous associated value is replaced.

        Args:
            key: The key to which to associate `value`.
            value: The value to be associated with `key`.
        """
        hash_value = hash(key)
        bucket_index = hash_value % self._buckets
        bucket = self._data[bucket_index]

        # Look for the key in the bucket
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Replace the old value
                return

        # Key not found, add a new key-value pair
        bucket.append((key, value))

    def __contains__(self, key):
        """Check whether `key` appears in the HashMap.

        Target Complexity: O(1) expected.

        Args:
            key: The key for which to check.

        Returns:
            True if `key` appears in the HashMap, False otherwise.
        """
        hash_value = hash(key)
        bucket_index = hash_value % self._buckets
        bucket = self._data[bucket_index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                return True
        return False # instead of using else; lets loop complete.


    def remove(self, key):
        """Removes and returns the value associated with `key` in the HashMap.

        Target Complexity: O(1) expected.

        Args:
            key: The key of the entry to remove.

        Returns:
            The value associated with `key`.

        Raises:
            KeyError: If the HashMap does not contain `key`.
        """
        hash_value = hash(key)
        bucket_index = hash_value % self._buckets
        bucket = self._data[bucket_index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i] # Remove the key-value pair entirely from the bucket
                return v # Return the value associated with the key
            
        raise KeyError("Cannot remove, Key not in HashMap.")


    def delete(self, key):
        """Deletes `key` from the HashMap, if present.

        Does nothing if key is not already present.

        Target Complexity: O(1) expected.

        Args:
            key: The key to be deleted.

        Returns:
            True if `key` was deleted, False if it was not present.
        """
        hash_value = hash(key)
        bucket_index = hash_value % self._buckets
        bucket = self._data[bucket_index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True

        return False


    def items(self):
        """Gets a list of all (key, value) pairs from the HashMap.

        No specific order is guaranteed.

        Returns:
            A list of all (key, value) pairs.
        """
        all_items = []
        
        for bucket in self._data:
            for kv in bucket:
                all_items.append(kv)
        
        return all_items
