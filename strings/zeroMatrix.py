def zeroMatrix(m):
    """
    m: a matrix
    
    If element in m x n matrix is zero, sets entire row and column to zero
    e.g. 1 2 3    1 2 0
         4 5 0 -> 0 0 0
         7 8 9    7 8 0
        
    Modifies matrix m
    Returns nothing
    """
    
    
    # Approach: Iterate over all elements of matrix, add row and column indices
    #   of zero-value elements to lists, then iterate over each list, setting
    #   all values in the row/column index to zero--O(m*n)
    
    rowsToZero = []
    colsToZero = []
    # Find zeroes in matrix
    for rowNo in range(len(m)):
        for colNo in range(len(m[rowNo])):
            # If zero, add row and column indices to lists
            if m[rowNo][colNo] == 0:
                if rowNo not in rowsToZero:
                    rowsToZero.append(rowNo)
                if colNo not in colsToZero:
                    colsToZero.append(colNo)
    
    # Set elements in rows/columns with listed indices to zero
    for rowNo in rowsToZero:
        for colNo in range(len(m[rowNo])):
            m[rowNo][colNo] = 0
    for colNo in colsToZero:
        for rowNo in range(len(m)):
            # Catch cases when matrix is jagged, or rows have different lengths
            if colNo < len(m[rowNo]):
                m[rowNo][colNo] = 0
    
    
#m = [[1, 2, 3], [4, 5, 0], [7, 8, 9]]
# Ans: [[1, 2, 0], [0, 0, 0], [7, 8, 0]]
#m = [[0, 2, 3], [4, 5, 0], [7, 8, 9]]
# Ans: [[0, 0, 0], [0, 0, 0], [0, 8, 0]]
#m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 0]]
# Ans: [[1, 2, 0, 4], [5, 6, 0, 8], [0, 0, 0]]
m = [[1, 0, 3, 4], [5, 0, 7, 8], [9, 10, 11, 12]]
# Ans: [[0, 0, 0, 0], [0, 0, 0, 0], [9, 0, 11, 12]]
zeroMatrix(m)
print(m)
