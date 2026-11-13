from vectors import dot, distance


#example of left & right: 
#left = [[3,2],
        #[1,3]]

#rigth = [[2,1],
#         [1,3]]


def multiply(left, right) -> list:

    if len(left[0]) == len(right):
        pass
    else:
        print("left matrix's columns does not equal to rigth matrix's rows")
        raise IndexError
    result = []
    columns_right = []
    for row in range (0, len(right[0])):
        column = []
        for col in range(0, len(right)):
            column.append(right[col][row])
        columns_right.append(column)

    for row in range(0, len(left)):
        list_rows = []
        for column in columns_right:
            list_rows.append(dot(left[row], column))
        result.append(list_rows)
    return result




scale_by_2 = [
    [2, 0],
    [0, 2],
]

identity = [
    [1, 0],
    [0, 1],
]
assert multiply(identity, scale_by_2) == scale_by_2
matrix = multiply(identity, scale_by_2)

square = [
    [ 1,  1, -1, -1],  # x of each point
    [ 1, -1, -1,  1],  # y of each point
]

multiply(scale_by_2, square) #doubles every one of those coordinates from square

rotate_90 = [
    [0, -1],
    [1,  0],
]
print(multiply(rotate_90, square)) #-> transform each column from [x,y] to [-y, x]
assert multiply(rotate_90, [[1], [0]]) == [[0], [1]]


#multiply by 2 the square and then rotate it:
scalated_and_rotated = multiply(rotate_90, multiply(scale_by_2, square))

print(scalated_and_rotated)
assert distance([scalated_and_rotated[0][0], scalated_and_rotated[1][0]], [0,0]) == distance([multiply(scale_by_2, square)[0][0], multiply(scale_by_2, square)[1][0]], [0,0])
#Check with distance that one rotated column is the same length from the origin as it was before

def draw_in_plane(matrix): #prints the matrix's points (each column is a point) in a plane drawn by "." & "#"
    #1. find the largest and shortest cord in each axis to draw the plain's dimensions
    largest_x = sorted(matrix[0])[len(matrix[0]) -1] #we use sorted instead of sort to avoid changing the original
    shortest_x = sorted(matrix[0])[0]

    largest_y = sorted(matrix[1])[len(matrix[0]) - 1]
    shortest_y = sorted(matrix[1])[0]

    plane = []
    cords = []
    #save each cord in a list to compare. 
    for axis in range(len(matrix[0])):
        cords.append((matrix[0][axis],matrix[1][axis]))
    
    for y in range(largest_y, shortest_y - 1, -1):
        print("")
        for x in range(shortest_x, largest_x +1):
            if (x, y) in cords:
                print("#", end="")
            else:
                print(".", end="")

draw_in_plane(square)
draw_in_plane(scalated_and_rotated)



