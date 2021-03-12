"""
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and 
column are set to O. 
Hints: # 17, #74, #102
"""
def zero_matrix(matrix):
    M = len(matrix)
    N = len(matrix[0])
    clear = []
    for m in range(M):
        for n in range(N):
            # we could add a test to skip those columns that we already know are zero. Cost not effective
            if not matrix[m][n]:
                clear.append((m,n))
                break

    for m, n in clear:
        for i in range(N):
            matrix[m][i] = 0
        for i in range(M):
            matrix[i][n] = 0

    return matrix 


if __name__ == "__main__":
    matrix = [[1, 2 , 0], [1, 0, 1], [1, 1 , 1]]
    print(zero_matrix(matrix))
