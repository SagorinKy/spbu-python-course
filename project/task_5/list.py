from collections.abc import MutableMapping
from typing import Any, Optional, Generator, List


class Node_For_Values:
    """
    Class to represent a data node in the value list.

    Each node holds a (key, value) pair and pointers to the next and previous nodes
    in the doubly linked list of values. This is used to store data inside the hash table,
    when two elements have the same hash.

    Attributes:
        data (Any): The data stored in the node.
        key (Any): The key associated with the data.
        next (Optional[Node_For_Values]): Reference to the next node in the value list.
        previous (Optional[Node_For_Values]): Reference to the previous node in the value list.
    """

    def __init__(self, key, data):
        self.data: Any = data
        self.key: Any = key
        self.next: Optional["Node_For_Values"] = None
        self.previous: Optional["Node_For_Values"] = None


class Node_For_Hash:
    """
    Class to represent a hash node in the hash table.

    Each node acts as a container for a value list of elements with the same hash.
    The node holds a hash and a doubly linked list of values, which can contain multiple
    (key, value) pairs if they share the same hash.

    Attributes:
        hash (int): The hash value for the data.
        data_head (Optional[Node_For_Values]): Reference to the first node in the value list.
        data_tail (Optional[Node_For_Values]): Reference to the last node in the value list.
        next (Optional[Node_For_Hash]): Reference to the next node in the hash table.
        previous (Optional[Node_For_Hash]): Reference to the previous node in the hash table.
        length (int): The number of elements in the value list for this hash.
    """

    def __init__(self, hash: int):
        self.hash: int = hash
        self.data_head: Optional["Node_For_Values"] = None
        self.data_tail: Optional["Node_For_Values"] = None

        self.next: Optional["Node_For_Hash"] = None
        self.previous: Optional["Node_For_Hash"] = None
        self.length: int = 0

    def find_value_node(self, key: Any, data: Any) -> Optional["Node_For_Values"]:
        """
        Searches for a node with the given key and data in the value list of this hash node.

        If a node with the specified key and data is found, it returns it. Otherwise, returns None.

        Arguments:
            key (Any): The key to search for.
            data (Any): The value to search for.

        Returns:
            Optional[Node_For_Values]: The node with the matching key and data, or None if not found.
        """
        node = self.data_head
        while node is not None:
            if node.key == hash(key) & node.data == data:
                return node
            node = node.next
        return None


class DoublyLinkedList(MutableMapping):
    """
    Hash table implementation using doubly linked lists.

    This class represents a hash table where each node is itself a doubly linked list. If two elements
    have the same hash, they will be stored in the same value list inside the corresponding hash node.

    Attributes:
        head (Optional[Node_For_Hash]): Reference to the first node in the hash table.
        tail (Optional[Node_For_Hash]): Reference to the last node in the hash table.
        length (int): The total number of elements in the hash table.
    """

    def __init__(self) -> None:
        """
        Initializes an empty hash table.
        """
        self.head: Optional["Node_For_Hash"] = None
        self.tail: Optional["Node_For_Hash"] = None
        self.length: int = 0

    def __getitem__(self, key: Any) -> Any:
        """
        Retrieves the data associated with the given key.

        If the key is not found, returns an empty list.

        Arguments:
            key (Any): The key to search for.

        Returns:
            Any: A list of values associated with the key.
        """
        list_node = self._find_hash_node(hash(key))
        if list_node is None:
            return []
        node = list_node.data_head
        data: List = []
        while node is not None:
            if node.key == key:
                data.append(node.data)
            node = node.next
        return data

    def __setitem__(self, key: Any, data: Any) -> None:
        """
        Sets the data for the given key.

        If no node with the given key exists, it will be added to the table.

        Arguments:
            key (Any): The key to associate with the data.
            data (Any): The data to associate with the key.
        """
        node = self._find_hash_node(hash(key))
        if node is None:
            self._append_node(key)
            node = self.tail
        if node is not None:
            data_node = node.find_value_node(key, data)
            if data_node is None:
                self._append_value(node, key, data)
                return

    def __delitem__(self, key: Any) -> None:
        """
        Deletes the element by key from the hash table.

        If an element with the given key is not found, raises a KeyError.

        Arguments:
            key (Any): The key to delete.
        """
        key_hash = hash(key)
        current = self.head
        while current is not None:
            if current.hash == key_hash:
                if current.previous is not None:
                    current.previous.next = current.next
                else:
                    self.head = current.next

                if current.next is not None:
                    current.next.previous = current.previous
                else:
                    self.tail = current.previous
                self.length -= 1
                return
            current = current.next

    def __iter__(self) -> Generator["Node_For_Values", None, None]:
        """
        Iterator over all values in the hash table.

        Yields all elements in the hash table starting from the first one.

        Returns:
            Generator[Node_For_Values]: A generator of all value nodes.
        """
        current = self.head
        while current is not None:
            node = current.data_head
            while node is not None:
                yield node
                node = node.next
            current = current.next

    def __reversed__(self) -> Generator["Node_For_Values", None, None]:
        """
        Iterator over all values in the hash table in reverse order.

        Yields all elements in the hash table starting from the last one.

        Returns:
            Generator[Node_For_Values]: A generator of all value nodes in reverse order.
        """
        current = self.tail
        while current is not None:
            node = current.data_tail
            while node is not None:
                yield node
                node = node.previous
            current = current.previous

    def __len__(self) -> int:
        """
        Returns the number of elements in the hash table.

        Returns:
            int: The number of elements in the hash table.
        """
        length = 0
        current = self.head
        while current is not None:
            length += current.length
            current = current.next
        return length

    def __contains__(self, key: Any) -> bool:
        """
        Checks if the given key exists in the hash table.

        Arguments:
            key (Any): The key to check for existence.

        Returns:
            bool: True if the key is in the table, False otherwise.
        """
        node = self._find_hash_node(hash(key))
        if node is not None:
            current = node.data_head
            while current:
                if current.key == key:
                    return True
                current = current.next
        return False

    def _append_value(self, node_hash: "Node_For_Hash", key: Any, data: Any) -> None:
        """
        Adds a new value to the end of value list of the given hash node.

        If a value with the given key does not already exist in the list, it will be added.

        Arguments:
            node_hash (Node_For_Hash): The hash node to append the value to.
            key (Any): The key for the new value.
            data (Any): The data to associate with the key.
        """
        new_node = Node_For_Values(key, data)
        if node_hash.data_tail is None:
            node_hash.data_head = new_node
            node_hash.data_tail = new_node
            node_hash.length += 1
        else:
            if node_hash.find_value_node(key, data) is None:
                node_hash.data_tail.next = new_node
                new_node.previous = node_hash.data_tail
                node_hash.data_tail = new_node
                node_hash.length += 1

    def _append_node(self, key: Any) -> None:
        """
        Appends a new hash node to the end of hash table.

        If a node with the given hash does not exist, it is created and appended to the table.

        Arguments:
            key (Any): The key for the new node.
        """
        node = Node_For_Hash(hash(key))
        if self.head is None or self.tail is None:
            self.head = node
            self.tail = node
        else:
            if self._find_hash_node(hash(key)) is None:
                self.tail.next = node
                node.previous = self.tail
                self.tail = node

    def _prepend_value(self, node_hash: "Node_For_Hash", key: Any, data: Any) -> None:
        """
        Adds a new value to the start of value list of the given hash node.

        If a value with the given key does not already exist in the list, it will be added.

        Arguments:
            node_hash (Node_For_Hash): The hash node to append the value to.
            key (Any): The key for the new value.
            data (Any): The data to associate with the key.
        """
        new_node = Node_For_Values(key, data)
        if node_hash.data_tail is None or node_hash.data_head is None:
            node_hash.data_head = new_node
            node_hash.data_tail = new_node
            node_hash.length += 1
        else:
            if node_hash.find_value_node(key, data) is None:
                node_hash.data_head.previous = new_node
                new_node.next = node_hash.data_head
                node_hash.data_head = new_node
                node_hash.length += 1

    def _prepend_node(self, key: Any) -> None:
        """
        Appends a new hash node to the start of hash table.

        If a node with the given hash does not exist, it is created and appended to the table.

        Arguments:
            key (Any): The key for the new node.
        """
        node = Node_For_Hash(hash(key))
        node.data_tail
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            if self._find_hash_node(hash(key)) is None:
                self.head.next = node
                node.next = self.head
                self.head = node

    def _find_hash_node(self, hash: int) -> Optional["Node_For_Hash"]:
        """
        Finds the hash node for the given hash value.

        Arguments:
            hash (int): The hash value to search for.

        Returns:
            Optional[Node_For_Hash]: The node with the matching hash, or None if not found.
        """
        node = self.head
        while node is not None:
            if node.hash == hash:
                return node
            node = node.next
        return None
