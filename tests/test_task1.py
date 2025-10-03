import pytest
import project.vectors as v
import project.matrices as m

def test_vector_length():
    vector = [2, 3, 6]
    assert 7 == v.vector_length

def test_scalar_product():
    vector_1 = [1, 6, 9]
    vector_2 = [3, 5, 10]
    assert 123 == v.scalar_product(vector_1, vector_2)

def test_angle_between_vectors():
    vector_1 = [1, 6, 9]
    vector_2 = [3, 5, 10]
    assert 0.08232482583638594 == v.angle_between_vectors(vector_1, vector_2)

def test_matrices_sum():
    matrix_1 = [[1, 2, 3], [1, 2, 3]]
    matrix_2 = [[8, 6, 4], [4, 2, 0]]
    assert m.matrices_sum(matrix_1, matrix_2) == [[9, 8, 7], [5, 4, 3]]

def test_matrices_product():
    matrix_1 = [[1, 2, 3], [3, 2, 1]]
    matrix_2 = [[8, 6] [4, 4] [2, 0]]
    assert m.matrices_sum(matrix_1, matrix_2) == [[22, 14], [34, 26]]

def test_transpose():
    matrix = [[5, 6, 7], [22, 34, 55], [1, 1, 1]]
    assert m.transpose(matrix) == [[5, 22, 1], [6, 34, 55], [7, 55, 1]]
