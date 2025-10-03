from math import acos

def vector_length (vector : list) -> float:
    """ Calculates vector's length by formulae ((x_1)^2 + ... + (x_n)^2)^0.5 """
    length_squared = 0
    for element in vector:
        length_squared += element ** 2
    return length_squared ** 0.5

def scalar_product (vector_1 : list, vector_2 : list) -> float:
    result = 0
    for i in range (0, min(len(vector_1), len(vector_2))):
        result += vector_1[i] * vector_2[i]
    return result

def angle_between_vectors (vector_1 : list, vector_2 : list) -> float:
    cos = scalar_product(vector_1, vector_2) / (vector_length(vector_1) * vector_length(vector_2))
    return acos(cos)