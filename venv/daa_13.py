import numpy as np
print("Jasmanjot Singh- 1706448")


def solve_n_queens(matrix, row):

    if row >= len(matrix):
        return True

    for i in range(len(matrix[row])):
        if safe_place(matrix, row, i):
            matrix[row][i] = 1
            if solve_n_queens(matrix, row+1):
                return True
            
            matrix[row][i] = 0


def safe_place(matrix, row, col):
    for i in range(col):
        if matrix[row][i] == 1:
            return False
    
    for i in range(row):
        if matrix[i][col] == 1:
            return False
    i,j = row-1,col-1
    while i >= 0 and j >= 0:
        if matrix[i][j] == 1:
            return False
        
        i -= 1
        j -= 1
    return True


def n_queens():
    n = 8
    matrix = np.zeros((n,n), dtype=np.int8)

    solve_n_queens(matrix,0)
    return matrix

matrix = n_queens()

print ('Solution for 8 queens is given by:-')
print(matrix)