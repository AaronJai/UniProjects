def land2(num_properties, legal_size_limit, properties):
    if num_properties == 0:
        return 0

    # Sort properties by value descending and size ascending
    properties.sort(key=lambda x: (-x[0], x[1]))

    merged_value = 0
    remaining_capacity = legal_size_limit

    for value, size in properties:
        if size <= remaining_capacity:
            merged_value = max(merged_value, value)  # Always take the highest value property
            remaining_capacity -= size

        if remaining_capacity == 0:
            break

    return merged_value

# Test 10: Large properties with varying sizes
n = 5
L = 10
properties = [(8, 6), (6, 4), (5, 2), (3, 3), (7, 1)]
print("Test 10 (Large and varied sizes) result:", land2(n, L, properties))  # Expected output: 8

# Test 12: Properties that can all merge into one
n = 6
L = 12
properties = [(5, 2), (3, 1), (2, 2), (4, 3), (6, 4), (1, 1)]
print("Test 12 (Merge all into one) result:", land2(n, L, properties))  # Expected output: 6

# Test 15: Equal values with different sizes
n = 4
L = 6
properties = [(4, 1), (4, 2), (4, 3), (4, 1)]
print("Test 15 (Equal values, different sizes) result:", land2(n, L, properties))  # Expected output: 4
