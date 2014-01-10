#[12-23-13] Challenge #140 [Intermediate] Graph Radius
#http://www.reddit.com/r/dailyprogrammer/comments/1tiz4z/122313_challenge_140_intermediate_graph_radius/

data = [x.strip().split() for x in open("challenge140I4.txt").readlines()]
matrix = data[1:]

def print_matrix(matrix):
    for row in matrix:
        print (row)
    print("")

def extend_matrix(matrix, limit):
    for i, row in enumerate(matrix):
        for j in range(len(matrix)):
            if i == j:
                matrix[i][j] = "X"
                continue
            if row[j] == "0":
                c = closest_connection(i,j)
                if int(c) == limit:
                    row[j] = c

def closest_connection(i, j):
    closest = 100
    for k in range(len(matrix)):
        if (k != i) and (k != j):
            if matrix[i][k] != "0" and int(matrix[i][k]) < closest:
                if matrix[k][j] != "0":
                    distance = int(matrix[i][k]) + int(matrix[k][j])
                    if distance < closest:
                        closest= distance
    return str(closest)

def find_radius():
    print("Starting matrix:")
    print_matrix(matrix)
    for x in range(2,len(matrix)):
        extend_matrix(matrix, x)
    print("Extended matrix:")
    print_matrix(matrix)
    radius = len(matrix)
    for row in matrix:
        eccentricity = 0
        for val in row:
            if val != "X" and int(val) > eccentricity:
                eccentricity = int(val)
        if eccentricity < radius:
            radius = eccentricity
    print("Radius:", radius)

find_radius()



