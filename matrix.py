matrix = [[1, 2, 3, 4 ],[ 5, 6, 7, 8 ],
              [ 9, 10, 11, 12 ],
              [ 13, 14, 15, 16 ]]

# matrix traversal
# it can be done by 2 for loops
# same no.of elements in every col
for i in range(len(matrix)):
    for j in range(len(matrix)):
        print(matrix[i][j])

# searching for element
a = 4
def fun1(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if a == matrix[i][j]:
                return "ele found"
    return "ele not found"

# printing diagonal of matrix
"""
top - bottom

left to right:
i == j
right to left:
(i+j) == (n-1)
"""
def left_right(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j:
                print(matrix[i][j], end=" ")
def right_left(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i+j == len(matrix)-1:
                print(matrix[i][j], end=" ")


# sorting a matrix
def sort_matrix(matrix):
    temp = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            temp.append(matrix[i][j])
    a = 0
    sorted_temp = sorted(temp)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] = sorted_temp[a]
            a+=1
    return matrix

# print(matrix[::-1])
# for i in range(5):
#     for j in range(5):
#         print(i,j)



## rotating matrix 180 degree
## first transpose then reversing it
def transpose(matrix):
    for i in range(len(matrix)):
        for j in range(i,len(matrix)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    return matrix
def rev(matrix):
    a = matrix[::-1]
    return a
one1 = transpose(matrix)
rev1 = rev(one1)
one2 = transpose(rev1)
rev2 = rev(one2)
print(matrix)