def adjacency_list_to_matrix(matrix):    
    n = len(matrix)

    # adj_matrix will be the output matrix
    adj_matrix = []

    # loop for the key value, from 0 to n
    for key in range(n):
        adj_matrix_line = []

        # loop to compare each element of the list
        for i in range(n):
            if i in matrix[key]:
                adj_matrix_line.append(1)
            else:
                adj_matrix_line.append(0)
        adj_matrix.append(adj_matrix_line)
        print(adj_matrix_line)

    return adj_matrix

# matrix sample:
matrix = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [2]
}

# example of usage:
adjacency_list_to_matrix(matrix)
