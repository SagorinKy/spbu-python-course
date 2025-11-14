from collections.abc import MutableMapping
from typing import Any, Optional, Generator, List


class Node_For_Values:
    def __init__(self, key, data):
        self.data: Any = data
        self.key: Any = key
        self.next: Optional["Node_For_Values"] = None
        self.previous: Optional["Node_For_Values"] = None


class Node_For_Hash:
    def __init__(self, hash: int):
        self.hash: int = hash
        self.data_head: Optional["Node_For_Values"] = None
        self.data_tail: Optional["Node_For_Values"] = None

        self.next: Optional["Node_For_Hash"] = None
        self.previous: Optional["Node_For_Hash"] = None
        self.length: int = 0

    def find_value_node(self, key: Any, data: Any) -> Optional["Node_For_Values"]:
        node = self.data_head
        while node is not None:
            if node.key == hash(key) & node.data == data:
                return node
            node = node.next
        return None


class DoublyLinkedList(MutableMapping):
    def __init__(self) -> None:
        self.head: Optional["Node_For_Hash"] = None
        self.tail: Optional["Node_For_Hash"] = None
        self.length: int = 0

    def __getitem__(self, key: Any) -> Any:
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
        current = self.head
        while current is not None:
            node = current.data_head
            while node is not None:
                yield node
                node = node.next
            current = current.next

    def __reversed__(self) -> Generator["Node_For_Values", None, None]:
        current = self.tail
        while current is not None:
            node = current.data_tail
            while node is not None:
                yield node
                node = node.previous
            current = current.previous

    def __len__(self) -> int:
        length = 0
        current = self.head
        while current is not None:
            length += current.length
            current = current.next
        return length

    def _append_value(self, node_hash: "Node_For_Hash", key: Any, data: Any) -> None:
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
        node = self.head
        while node is not None:
            if node.hash == hash:
                return node
            node = node.next
        return None
