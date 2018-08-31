def rotateMatrix(m):
    """
    m: a square matrix, a list of lists
    
    Rotates matrix by 90 degrees
    e.g. 1 2 3    7 4 1
         4 5 6 -> 8 5 2
         7 8 9    9 6 3
    
    Modifies matrix m
    Returns nothing
    """
    dim = len(m) # Length of sides of matrix
    
    # Validate input
    if dim == 0:
        return
    # Make sure input is a square matrix
    else:
        for row in m:
            if len(row) != dim:
                return
    
    # Approach: Transpose then flip vertically--O(n^2)
    # Start: 1 2 3
    #        4 5 6
    #        7 8 9
    
    # Transpose: Swap upper right triangle with lower left,
    #   keep main diagonal as is
    #        1 4 7
    #        2 5 8
    #        3 6 9
    for rowIndex in range(dim):
        for colIndex in range(rowIndex + 1, dim):
            temp = m[rowIndex][colIndex]
            m[rowIndex][colIndex] = m[colIndex][rowIndex]
            m[colIndex][rowIndex] = temp
    # Flip horizontally
    #        7 4 1
    #        8 5 2
    #        9 6 3
    for rowIndex in range(dim):
        for colIndex in range(dim // 2):
            temp = m[rowIndex][colIndex]
            m[rowIndex][colIndex] = m[rowIndex][dim - colIndex - 1]
            m[rowIndex][dim - colIndex - 1] = temp
            

#m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Ans: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# Ans: [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]
# Test: Invalid input (non-square matrices)
#m = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
#m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
rotateMatrix(m)
print(m)
