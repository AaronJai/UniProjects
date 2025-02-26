"""
notes
1st line: 
    1st int = number of properties, 2nd int = legal property size limit.
next n lines:
    1st int = property value, 2nd int = property size.

tax is sum of their values, can minimise tax by merging two adjacemy properties..
value = maximum of the two and size = sum of the two.
size cannot be larger than legal limit; no limitations on amount of merges otherwise
"""

from collections import deque

# def land2(num_properties, legal_size_limit, properties):
    
#     if num_properties == 0:
#         return 0
    
#     merged_properties = []
    
#     for value, size in properties:
#         while merged_properties and merged_properties[-1][1] + size <= legal_size_limit:
#            prev_value, prev_size = merged_properties.pop()
#            size += prev_size
#            value = max(value, prev_value)
           
#         merged_properties.append((value, size))
    
#     total_tax_paid = sum(value for value, size in merged_properties)
    
#     return total_tax_paid
        

# def land2(num_properties, legal_size_limit, properties):
#     # DP arra
#     dp = [float('inf')] * (num_properties + 1)
#     dp[0] = 0  # No tax for 0 properties
    
#     # loop through each property
#     for i in range(1, num_properties + 1):
#         max_value = 0
#         total_size = 0
        
#         # Try merge, going backward
#         for j in range(i, 0, -1):
#             total_size += properties[j - 1][1]  # Add the size of property j
#             if total_size > legal_size_limit:
#                 break  # Stop merging if the size exceeds the limit
            
#             # Update the maximum value
#             max_value = max(max_value, properties[j - 1][0])
            
#             # Update dp[i] by considering merging properties j..i
#             dp[i] = min(dp[i], dp[j - 1] + max_value)

#     return dp[num_properties]

#######################################
# CODE HAS ONLY SO FAR BEEN CONSIDERING MERGING LEFT TO RIGHT INSTEAD OF PICKING OPTIMALLY

# def land2(num_properties, legal_size_limit, properties):
#     if num_properties == 0:
#         return 0

#     # Sort properties by value in descending order
#     properties = sorted(properties, reverse=True, key=lambda x: x[0])

#     merged_properties = []

#     while properties:
#         # Take the property with the highest value
#         value, size = properties.pop(0)
        
#         # Try to find another property to merge with
#         for i in range(len(properties)):
#             if size + properties[i][1] <= legal_size_limit:
#                 # Merge with the property that has the highest value that fits
#                 size += properties[i][1]
#                 value = max(value, properties[i][0])
#                 properties.pop(i)
#                 break

#         # Add the merged property
#         merged_properties.append((value, size))

#     # Calculate total tax paid
#     total_tax_paid = sum(value for value, size in merged_properties)

#     return total_tax_paid

###########################################################
# ABOVE WASN'T MERGING MULTIPLE PROPETIES TOGETHER 

# def land2(num_properties, legal_size_limit, properties):
#     if num_properties == 0:
#         return 0

#     # Sort properties by value in descending order
#     properties = sorted(properties, reverse=True, key=lambda x: x[0])

#     merged_properties = []

#     while properties:
#         # Take the property with the highest value
#         value, size = properties.pop(0)

#         # Merge within limit
#         merged = True
#         while merged:
#             merged = False
#             for i in range(len(properties)):
#                 if size + properties[i][1] <= legal_size_limit:
#                     # Merge with the property that has the highest value that fits
#                     size += properties[i][1]
#                     value = max(value, properties[i][0])
#                     properties.pop(i)
#                     merged = True
#                     break

#         # Add the merged property
#         merged_properties.append((value, size))

#     # Calculate total tax paid
#     total_tax_paid = sum(value for value, size in merged_properties)

#     return total_tax_paid

def land2(num_properties, legal_size_limit, properties):
    if num_properties == 0:
        return 0

    # Sort properties by size first, then by value descending
    properties.sort(key=lambda x: (x[1], -x[0]))

    merged_properties = []
    i = 0

    while i < len(properties):
        value, size = properties[i]
        current_value = value
        current_size = size

        # Try to merge with other properties while staying within the legal size limit
        j = i + 1
        while j < len(properties) and current_size + properties[j][1] <= legal_size_limit:
            current_size += properties[j][1]
            current_value = max(current_value, properties[j][0])
            j += 1

        merged_properties.append((current_value, current_size))
        i = j

    total_value = sum(value for value, size in merged_properties)
    return total_value

# num_properties, legal_size_limit = map(int, input().split())
# properties = [tuple(map(int, input().split())) for _ in range(num_properties)]
# print(land2(num_properties, legal_size_limit, properties))

#test 1
num_properties = 3
legal_size_limit = 3
properties = [(1, 1), (2, 2), (3, 3)]
print("Test 1 result:", land2(num_properties, legal_size_limit, properties)) # Expected output: 5

# Test 2
n = 4
L = 5
properties = [(2, 4), (2, 4), (1, 2), (3, 3)]
print("Test 2 result:", land2(n, L, properties)) # Expected input: 7

## EXTRA TESTS

# Test 3: All properties can merge
n = 3
L = 10
properties = [(5, 1), (6, 2), (4, 3)]
print("Test 3 (All can merge) result:", land2(n, L, properties))  # Expected output: 6

# Test 4: All properties have the same value and size
n = 4
L = 10
properties = [(2, 2), (2, 2), (2, 2), (2, 2)]
print("Test 4 (Same value/size) result:", land2(n, L, properties))  # Expected output: 2

# # Large Test: Test with many properties that can be merged
# n = 200000
# L = 1000
# properties = [(i % 10, 1) for i in range(n)]  # Properties with alternating values but small sizes
# print("Test Large result:", land2(n, L, properties))  # Expected: Result should be a value ≤ 9

# test 5
n = 3
L = 5
properties = [(3, 2), (1, 2), (4, 2)]
print("Test 5 (Optimal merge) result:", land2(n, L, properties))  # Expected output: 5

# Additional Test Cases

# Test 6: No merging needed (single property)
n = 1
L = 10
properties = [(10, 5)]
print("Test 6 (Single property) result:", land2(n, L, properties))  # Expected output: 10

# Test 7: All properties too large to merge
n = 3
L = 3
properties = [(5, 3), (6, 3), (4, 3)]
print("Test 7 (No merges possible) result:", land2(n, L, properties))  # Expected output: 15

# Test 8: Small properties, many possible merges
n = 5
L = 10
properties = [(1, 2), (2, 3), (3, 1), (4, 2), (5, 1)]
print("Test 8 (Many small properties) result:", land2(n, L, properties))  # Expected output: 5

# Test 9: Properties already sorted in ascending order
n = 4
L = 6
properties = [(1, 1), (2, 1), (3, 2), (4, 1)]
print("Test 9 (Ascending order) result:", land2(n, L, properties))  # Expected output: 4

# Test 10: Large properties with varying sizes
n = 5
L = 10
properties = [(8, 6), (6, 4), (5, 2), (3, 3), (7, 1)]
print("Test 10 (Large and varied sizes) result:", land2(n, L, properties))  # Expected output: 8

# Test 11: Some properties with zero value
n = 4
L = 10
properties = [(0, 2), (7, 3), (0, 1), (6, 4)]
print("Test 11 (Zero value properties) result:", land2(n, L, properties))  # Expected output: 7

# Test 12: Properties that can all merge into one
n = 6
L = 12
properties = [(5, 2), (3, 1), (2, 2), (4, 3), (6, 4), (1, 1)]
print("Test 12 (Merge all into one) result:", land2(n, L, properties))  # Expected output: 6

# Test 13: No properties (empty input)
n = 0
L = 5
properties = []
print("Test 13 (Empty properties) result:", land2(n, L, properties))  # Expected output: 0

# Test 14: Max value is the smallest property
n = 3
L = 7
properties = [(1, 2), (2, 3), (10, 1)]
print("Test 14 (Max value smallest property) result:", land2(n, L, properties))  # Expected output: 10

# Test 15: Equal values with different sizes
n = 4
L = 6
properties = [(4, 1), (4, 2), (4, 3), (4, 1)]
print("Test 15 (Equal values, different sizes) result:", land2(n, L, properties))  # Expected output: 4
