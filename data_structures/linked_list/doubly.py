from __future__ import annotations

from collections.abc import Iterator, Reversible
from typing import Any, Optional

from data_structures.exceptions import LinkedListIndexError
from data_structures.linked_list import LinkedList
from data_structures.linked_list.nodes import DoublyNode


class DoublyLinkedListIterator(Iterator):
    """

    """

    def __init__(self, doubly_linked_list: DoublyLinkedList):
        """

        :param doubly_linked_list:
        :type doubly_linked_list: DoublyLinkedList
        """
        self.doubly_linked_list = doubly_linked_list
        self.current: Optional[DoublyNode] = self.doubly_linked_list.head

    def __next__(self) -> DoublyNode:
        """

        :return:
        :rtype: Node
        """
        if self.current is not None:
            current: Optional[DoublyNode] = self.current
            self.current = current.next
            return current
        else:
            raise StopIteration


class DoublyLinkedListReversedIterator(DoublyLinkedListIterator):
    """

    """

    def __init__(self, doubly_linked_list: DoublyLinkedList):
        """

        :param doubly_linked_list:
        :type doubly_linked_list: DoublyLinkedList
        """
        super().__init__(doubly_linked_list)

        node: Optional[DoublyNode] = None
        for node in self.doubly_linked_list:
            pass
        else:
            self.current = node

    def __next__(self) -> DoublyNode:
        """

        :return:
        :rtype: DoublyNode
        """
        if self.current is not None:
            current: Optional[DoublyNode] = self.current
            self.current = current.previous
            return current
        else:
            raise StopIteration


class DoublyLinkedListSearchIterator(DoublyLinkedListIterator):
    """

    """

    def __init__(self, doubly_linked_list: DoublyLinkedList, value: Any):
        """

        :param doubly_linked_list:
        :type doubly_linked_list: SinglyLinkedList
        :param value:
        :type value: Any
        """
        super().__init__(doubly_linked_list)
        self.value = value

    def __next__(self) -> DoublyNode:
        """

        :return:
        :rtype: Node
        """
        while True:
            current: Optional[DoublyNode] = self.current
            try:
                self.current = current.next
            except AttributeError:  # if the singly linked list is empty
                raise StopIteration
            if current.value == self.value:
                return current
            if current.next is None:
                raise StopIteration


class DoublyLinkedList(LinkedList, Reversible):
    def _init(self, *args) -> None:
        if args:
            self.head = DoublyNode(value=args[0])
            current_node = self.head
            for i in args[1:]:
                current_node = DoublyNode(i, previous=current_node)

    def __iter__(self) -> DoublyLinkedListIterator:
        """

        :return:
        :rtype: DoublyLinkedListIterator
        """
        return DoublyLinkedListIterator(self)

    def __reversed__(self) -> DoublyLinkedListReversedIterator:
        """

        :return:
        :rtype: DoublyLinkedListReversedIterator
        """
        return DoublyLinkedListReversedIterator(self)

    def append(self, value: Any) -> None:
        if self:
            DoublyNode.after_node(value, self.tail)
        else:
            self.head = DoublyNode(value)

    def pop(self) -> Optional[DoublyNode]:
        if not self:  # this doubly linked list is empty
            raise LinkedListIndexError
        elif len(self) == 1:
            node = self.head
            self.head = None
            return node
        else:
            tail = self.tail

            new_tail = tail.previous
            new_tail.next = None

            return tail

    def reverse(self) -> None:
        """
        In-place reverse

        :return:
        :rtype: None
        """
        tail = self.tail
        for node in self:
            node.next, node.previous = node.previous, node.next

        self.head = tail

    def search_iter(self, value: Any) -> DoublyLinkedListSearchIterator:
        """
        Search for a given value, return a iterator

        :param value:
        :type value: Any
        :return:
        :rtype: Generator[Node, None, None]
        """
        return DoublyLinkedListSearchIterator(self, value)
