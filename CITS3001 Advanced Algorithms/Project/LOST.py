"""
notes
input:
1st line = num of rows and cols in original matrix
2nd line = sum of rows,
3rd line = sum of cols
"""

def lost(size_of_matrix, row_sums, col_sums):
    # #initialise matrix
    matrix = []
    for i in range(size_of_matrix):
        row = [0] * size_of_matrix
        matrix.append(row)
    
    for i in range(size_of_matrix):
        for j in range(size_of_matrix):
            
            # value at [i][j] is the minimum of the sum of the row and col
            value = min(row_sums[i], col_sums[j])
            matrix[i][j] = value
            
            row_sums[i] -= value
            col_sums[j] -= value
    
    # all() returns True if all items in an iterable are true, otherwise it returns False
    if all(s == 0 for s in row_sums) and all(s == 0 for s in col_sums):
        for row in matrix:
            print(" ".join(map(str, row)))
    else:
        print(-1)


size_of_matrix = int(input())
row_sums = list(map(int, input().split()))
col_sums = list(map(int, input().split()))
lost(size_of_matrix, row_sums, col_sums)

# # Test case 1
# size_of_matrix = 4
# row_sums = [1, 2, 3, 4]
# col_sums = [4, 3, 2, 1]

# lost(size_of_matrix, row_sums, col_sums)

# # Test case 2
# size_of_matrix = 3
# row_sums = [1, 5, 4]
# col_sums = [2, 3, 4]
# lost(size_of_matrix, row_sums, col_sums)
