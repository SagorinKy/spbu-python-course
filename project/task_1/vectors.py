from math import acos
from typing import List
from typing import Optional


def vector_length(vector: List[Optional[float | int]]) -> float:
    """
    Calculates vector's length by formulae ((x_1)^2 + ... + (x_n)^2)^0.5

    Parameters:
        vector (List): vector
    Returns:
        float: vector length
    """
    length_squared = 0
    for element in vector:
        length_squared += element**2
    return length_squared**0.5


def scalar_product(
    vector_1: List[Optional[float | int]], vector_2: List[Optional[float | int]]
) -> float:
    """
    Calculates scalar product of two vectors
    If one is longer than another one we assume all missing elements are 0

    Parameters:
        vector_1 (List[Optional [float | int] ]): first vector
        vector_2 (List[Optional [float | int] ]): second vector
    Returns:
        float | int: scalar product
    """

    result = 0
    for i in range(0, min(len(vector_1), len(vector_2))):
        result += vector_1[i] * vector_2[i]
    return result


def angle_between_vectors(
    vector_1: List[Optional[float | int]], vector_2: List[Optional[float | int]]
) -> float:
    """
    Calculates angle between vectors by formulae
    angle = arccos(scalar product / product of vector length)


    Parameters:
        vector_1 (List[Optional [float | int] ]): first vector
        vector_2 (List[Optional [float | int] ]): second vector
    Returns:
        float | int: angle between vectors
    """

    cos = scalar_product(vector_1, vector_2) / (
        vector_length(vector_1) * vector_length(vector_2)
    )
    return acos(cos)
