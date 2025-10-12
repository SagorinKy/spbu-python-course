"""
Test module for matrix operations.
Contains unit tests for matrix functions: addition, multiplication, transposition.
"""
import pytest
import project.task_1.matrices as m


def test_matrices_sum():
    """Test for matrices addition"""
    matrix_1 = [[1, 2, 3], [1, 2, 3]]
    matrix_2 = [[8, 6, 4], [4, 2, 0]]
    assert m.matrices_sum(matrix_1, matrix_2) == [[9, 8, 7], [5, 4, 3]]


def test_matrices_product():
    """Test for matrices multiplication"""
    matrix_1 = [[1, 2, 3], [3, 2, 1]]
    matrix_2 = [[8, 6], [4, 4], [2, 0]]
    assert m.matrices_product(matrix_1, matrix_2) == [[22, 14], [34, 26]]


def test_transpose():
    """Test for matrixs"""
    matrix = [[5, 6, 7], [22, 34, 55], [1, 1, 1]]
    assert m.transpose(matrix) == [[5, 22, 1], [6, 34, 1], [7, 55, 1]]
