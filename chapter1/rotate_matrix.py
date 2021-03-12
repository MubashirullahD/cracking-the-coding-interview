"""
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 
bytes, write a method to rotate the image by 90 degrees. (Can you do this in place? 
Hints: #51, #100
[[0, 1],    [x, y] ->     [y, x]
 [1, 0]]
 cos(theta), 1
 1, cos(theta)
 
 matrix = [[1, 2, 3], 
           [4, 5, 6], 
           [7, 8, 9]]
 matrix =[[3, 2, 1], 
          [6, 5, 4], 
          [9, 8, 7]]

rotated =[[3, 6, 9], 
          [2, 5, 8], 
          [1, 4, 7]]
"""
import copy
    
def rotate_matrix(image):
    # Copy method one
    copy_image_one = copy.deepcopy(image)
    print("Original", matrix)
    print("Copy of original", copy_image_one)
    N = len(matrix)

    # Part 1, reverse order within each row
    for row in range(N):
        for column in range(N):
            copy_image_one[row][column] = image[row][N-column-1]

    print("After modification")
    print("Original", matrix)    
    print("Copy", copy_image_one)


    # Copy method two
    copy_image_two = [list(row) for row in copy_image_one]
    # Test on what happens when you remove list? from the above code.


    # Part 2, transpose
    for row in range(N):
        for column in range(N):
            copy_image_two[column][row] = copy_image_one[row][column]
    
    return copy_image_two


def rotate_matrix_inplace(image):
    # Copy method one
    print("Original", matrix)
    N = len(matrix)

    # Part 1, reverse order within each row
    for row in range(N):
        for column in range(N//2):
            tmp = image[row][column]
            image[row][column] = image[row][N-column-1]
            image[row][N-column-1] = tmp

    print("After reversing")
    print("Original", matrix)


    # Part 2, transpose
    for row in range(N):
        for column in range(row, N):
            tmp = matrix[column][row]
            matrix[column][row] = matrix[row][column]
            matrix[row][column] = tmp
    
    return matrix


if __name__ == "__main__":
    matrix = [[1,2,3],
             [4,5,6],
             [7,8,9]]
    print("Rotated image", rotate_matrix_inplace(matrix))
    