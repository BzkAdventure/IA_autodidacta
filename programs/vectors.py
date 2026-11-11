

def distance(a:list, b:list) -> float:
    #each point a & b are points; lists of 2 axis (f.ex a = [3,4] and b = [0,0])
    difference = []
    try:
        difference.append(a[0] - b[0])
        difference.append(a[1] -b[1])
        length:float = (difference[0]**2 + difference[1]**2)**0.5
        return length
    except IndexError:
        raise IndexError

length_3_4 = distance([3,4], [0,0])
print(length_3_4)


def dot(a:list, b:list) ->float:
    #without error control
    product_1, product_2 = a[0] * b[0], a[1] * b[1]
    result = product_1 + product_2

    #as we have it now, the result also grows with the lengths. We have to divide the result
    #with distance(a, [0,0]) * distance (b, [0,0]) -> later
    return result

opposite = dot([3,3],[-3,-3]) #should be -18, negative, as they point opposite ways
print(opposite)

perpendicular = dot([3,3],[-3,3]) #should be 0, as they point perpendicular ways
print(perpendicular)

def cosine(a, b) ->float:
    try: 
        return dot(a, b) / (distance(a, [0,0]) * distance(b, [0,0]))
    except ZeroDivisionError:
        print("Error: Can not divide /0")

#cosine: delete the differences of 2 pairs of vectors that have the same angle. 

def nearest(points:list, query: list) -> list:
    minor_dist = points[0]
    for i in range (1, len(points)):
        dist = distance(points[i], query)
        if distance(minor_dist, query) > dist:
            minor_dist = points[i]
    return minor_dist
    
#returns the nearest point to the query. 
nearest_var = nearest([[0, 0], [3, 1], [10, 10]], [2, 0])
print(nearest_var)
