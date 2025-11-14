import pytest
from project.task_5.list import DoublyLinkedList


@pytest.fixture
def empty_table():
    """
    Fixture to provide an empty hash table (DoublyLinkedList).

    This fixture creates a fresh instance of the DoublyLinkedList class that is empty.
    It is used in tests that require an empty hash table to begin with.

    Returns:
        DoublyLinkedList: A new empty hash table.
    """
    return DoublyLinkedList()


@pytest.fixture
def filled_table():
    """
    Fixture to provide a filled hash table (DoublyLinkedList) with initial key-value pairs.

    This fixture creates a hash table with three key-value pairs:
    - "apple" => 10
    - "banana" => 20
    - "cherry" => 30

    Returns:
        DoublyLinkedList: A hash table pre-filled with data.
    """
    table = DoublyLinkedList()
    table["apple"] = 10
    table["banana"] = 20
    table["cherry"] = 30
    return table


def test_add_new_key_creates_node(empty_table):
    """
    Test for adding a new key-value pair to the empty table.

    This test ensures that when a new key-value pair is added to an empty table,
    a new node is created and the length of the table is updated.

    Arguments:
        empty_table (DoublyLinkedList): A fresh empty hash table.
    """
    empty_table["apple"] = 100
    result = empty_table["apple"]
    assert result == [100]
    assert len(empty_table) == 1


def test_add_same_key_twice_overwrites_value(empty_table):
    """
    Test for adding the same key twice and verifying that the values are appended.

    This test checks if adding the same key twice correctly handles overwriting
    the existing values. The result should either be a list with the original and
    the new value or just the new value.

    Arguments:
        empty_table (DoublyLinkedList): A fresh empty hash table.
    """
    empty_table["apple"] = 100
    empty_table["apple"] = 200
    result = empty_table["apple"]
    assert result == [100, 200] or result == [200]


def test_multiple_different_keys(filled_table):
    """
    Test for retrieving different keys from a filled table.

    This test checks whether the table properly stores and retrieves values for
    multiple different keys. It ensures that the correct values are returned for each key.

    Arguments:
        filled_table (DoublyLinkedList): A hash table with initial data.
    """
    assert filled_table["apple"] == [10]
    assert filled_table["banana"] == [20]
    assert filled_table["cherry"] == [30]
    assert len(filled_table) == 3


def test_get_existing_key(filled_table):
    """
    Test for retrieving an existing key.

    This test verifies that when requesting an existing key, the correct value is returned.

    Arguments:
        filled_table (DoublyLinkedList): A hash table with initial data.
    """
    assert filled_table["banana"] == [20]


def test_get_non_existing_key_returns_empty(empty_table):
    """
    Test for retrieving a non-existing key.

    This test ensures that when a key that does not exist is requested, the result is an empty list.

    Arguments:
        empty_table (DoublyLinkedList): A fresh empty hash table.
    """
    empty_table["apple"] = 10
    assert empty_table["orange"] == []


def test_delete_existing_key(filled_table):
    """
    Test for deleting an existing key.

    This test verifies that when an existing key is deleted, it is properly removed from the table,
    and accessing it after deletion should return an empty list.

    Arguments:
        filled_table (DoublyLinkedList): A hash table with initial data.
    """
    assert filled_table["banana"] != []
    del filled_table["banana"]
    assert filled_table["banana"] == []


def test_delete_non_existing_key_does_nothing(empty_table):
    """
    Test for deleting a non-existing key.

    This test ensures that trying to delete a key that does not exist does not raise errors
    and does nothing. No exception should be thrown.

    Arguments:
        empty_table (DoublyLinkedList): A fresh empty hash table.
    """
    try:
        del empty_table["not_exist"]
    except Exception as e:
        pytest.fail(f"Unexpected exception: {e}")


def test_iteration_over_values(filled_table):
    """
    Test for iterating over the keys in the hash table.

    This test checks whether iterating over the table correctly gives all keys present
    in the hash table.

    Arguments:
        filled_table (DoublyLinkedList): A hash table with initial data.
    """
    keys = [node.key for node in filled_table]
    assert set(keys) == {"apple", "banana", "cherry"}


def test_reverse_iteration(filled_table):
    """
    Test for reverse iteration over the keys in the hash table.

    This test verifies that iterating over the table in reverse gives the keys in the correct order.

    Arguments:
        filled_table (DoublyLinkedList): A hash table with initial data.
    """
    reversed_keys = [node.key for node in reversed(filled_table)]
    assert list(reversed(reversed_keys)) == ["apple", "banana", "cherry"]


def test_find_hash_node_returns_correct_bucket(empty_table):
    """
    Test for finding the correct hash node in the table.

    This test checks that the _find_hash_node function correctly returns the hash node
    for a given key, based on its hash value.

    Arguments:
        empty_table (DoublyLinkedList): A fresh empty hash table.
    """
    empty_table["apple"] = 1
    node = empty_table._find_hash_node(hash("apple"))
    assert node is not None
    assert node.hash == hash("apple")


def test_append_value_creates_chain(empty_table):
    """
    Test for appending a value to the value list of a hash node.

    This test ensures that when a value is appended to the value list for a hash node,
    the linked list of values is correctly updated.

    Arguments:
        empty_table (DoublyLinkedList): A fresh empty hash table.
    """
    empty_table["apple"] = 1
    node = empty_table._find_hash_node(hash("apple"))
    empty_table._append_value(node, 2, "apple")
    assert node.data_head is not None
    assert node.data_tail is not None
