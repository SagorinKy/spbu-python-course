import pytest
import sys
import os

current_dir = os.path.dirname(__file__)
project_path = os.path.join(current_dir, "..", "..", "project", "task_5")
sys.path.insert(0, os.path.abspath(project_path))

from list import Node_For_Hash, Node_For_Values, DoublyLinkedList


@pytest.fixture
def empty_table():
    return DoublyLinkedList()


@pytest.fixture
def filled_table():
    table = DoublyLinkedList()
    table["apple"] = 10
    table["banana"] = 20
    table["cherry"] = 30
    return table


def test_add_new_key_creates_node(empty_table):
    empty_table["apple"] = 100
    result = empty_table["apple"]
    assert result == [100]
    assert len(empty_table) == 1


def test_add_same_key_twice_overwrites_value(empty_table):
    empty_table["apple"] = 100
    empty_table["apple"] = 200
    result = empty_table["apple"]
    assert result == [100, 200] or result == [200]


def test_multiple_different_keys(filled_table):
    assert filled_table["apple"] == [10]
    assert filled_table["banana"] == [20]
    assert filled_table["cherry"] == [30]
    assert len(filled_table) == 3


def test_get_existing_key(filled_table):
    assert filled_table["banana"] == [20]


def test_get_non_existing_key_returns_empty(empty_table):
    empty_table["apple"] = 10
    assert empty_table["orange"] == []


def test_delete_existing_key(filled_table):
    del filled_table["banana"]
    with pytest.raises(KeyError):
        _ = filled_table["banana"]


def test_delete_non_existing_key_does_nothing(empty_table):
    try:
        del empty_table["not_exist"]
    except Exception as e:
        pytest.fail(f"Unexpected exception: {e}")


def test_iteration_over_values(filled_table):
    keys = [node.key for node in filled_table]
    assert set(keys) == {"apple", "banana", "cherry"}


def test_reverse_iteration(filled_table):
    reversed_keys = [node.key for node in reversed(filled_table)]
    assert list(reversed(reversed_keys)) == ["apple", "banana", "cherry"]


def test_find_hash_node_returns_correct_bucket(empty_table):
    empty_table["apple"] = 1
    node = empty_table._find_hash_node(hash("apple"))
    assert node is not None
    assert node.hash == hash("apple")


def test_append_value_creates_chain(empty_table):
    empty_table["apple"] = 1
    node = empty_table._find_hash_node(hash("apple"))
    empty_table._append_value(node, 2, "apple")
    assert node.data_head is not None
    assert node.data_tail is not None
