from .vectors import scalar_product
from typing import List
from typing import Union


def matrices_sum(
    matrix_1: List[List[Union[float | int]]],
    matrix_2: List[List[Union[float | int]]],
) -> List[List[Union[float | int]]]:
    """
    Adds to the elements of first matrix values from the corresponding elements of second one

    Parameters:
        matrix_1 (List[List[Union [float | int] ]]): first matrix
        matrix_2 (List[List[Union [float | int] ]]): second matrix
    Returns:
        List[List[Union [float | int] ]]: matrix that is sum of two matrix
    """

    for i in range(min(len(matrix_1), len(matrix_2))):
        for j in range(min(len(matrix_1[i]), len(matrix_2[i]))):
            matrix_1[i][j] += matrix_2[i][j]
    return matrix_1


def matrices_product(
    matrix_1: List[List[Union[float | int]]],
    matrix_2: List[List[Union[float | int]]],
) -> List[List[Union[float | int]]]:
    """
    if raw number of first matrix is equal to line number in second matrix
    return their product
    otherwise returns None

    Parameters:
        matrix_1 (List[List[Union [float | int] ]]): first matrix
        matrix_2 (List[List[Union [float | int] ]]): second matrix
    Returns:
        List[List]: matrix that is product of two matrix
    """
    result_matrix: List[List[Union[float | int]]] = []
    if len(matrix_1[0]) == len(matrix_2):
        for i in range(len(matrix_1)):
            result_matrix.append([])
            for j in range(len(matrix_2[0])):
                row = [matrix_2[l][j] for l in range(len(matrix_2))]
                result_matrix[i].append(scalar_product(matrix_1[i], row))
        return result_matrix
    return [[]]


def transpose(
    matrix: List[List[Union[float | int]]],
) -> List[List[Union[float | int]]]:
    """
    Transpose a matrix


    Parameters:
        matrix (List[List[Union [float | int] ]]): matrix
    Returns:
        List[List[Union [float | int] ]]: tranposed matrix
    """
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
