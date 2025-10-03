from vectors import scalar_product

def matrices_sum (matrix_1 : list[list], matrix_2 : list[list]) -> list[list]:
    """Adds to the elements of first matrix values from the corresponding elements of second one"""
    
    for i in range(min(len(matrix_1), len(matrix_2))):
        for j in range(min(len(matrix_1[i]), len(matrix_2)[i])):
            matrix_1[i][j] += matrix_2[i][j]
    return matrix_1

def matrices_product (matrix_1 : list[list], matrix_2 : list[list]) -> list[list]:
    """
    if raw number of first matrix is equal to line number in second matrix
    return their product
    otherwise returns None
    """
    result_matrix = []
    if len(matrix_1[0]) == len(matrix_2):
        for i in range(len(matrix_1)):
            result_matrix.append([])
            for j in range(len(matrix_2[0])):
                row = [matrix_2[l][j] for l in range(len(matrix_2))]
                result_matrix[i].append(scalar_product(matrix_1[i], row))
        return result_matrix
    return None

def transpose (matrix : list[list]) -> list[list]:
    """Transpose a matrix"""
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]