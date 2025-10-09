"""
Test module for vector operations.
Contains unit tests for matrix functions: addition, multiplication, transposition.
"""
import pytest
import project.vectors as v
from math import acos


def test_vector_length():
    """Test for vector length"""
    vector = [2, 3, 6]
    assert 7.0 == v.vector_length(vector)


def test_scalar_product():
    """Test for vectors scalar product"""
    vector_1 = [1, 6, 9]
    vector_2 = [3, 5, 10]
    assert 123 == v.scalar_product(vector_1, vector_2)


def test_angle_between_vectors():
    """Test for finding angle between vectors"""
    vector_1 = [1, 6, 9]
    vector_2 = [3, 5, 10]
    assert acos(123 / ((118**0.5) * (134**0.5))) == v.angle_between_vectors(
        vector_1, vector_2
    )
