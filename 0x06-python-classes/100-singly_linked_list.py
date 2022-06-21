#!/usr/bin/python3
"""
Singly Linked List Module
"""


class Node:
    """Defines a node of a singly linked list
    """
    def __init__(self, data, next_node=None):
        """Initialize the node object
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve data attribute for Node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Setter for data attribute for Node
        """
        if type(value) is not int:
            raise TypeError('data must be an integer')

        self.__data = value

    @property
    def next_node(self):
        """Getter for next node for Node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter for next_node attribute for Node
        """
        if value is not None and type(value) is not Node:
            raise TypeError('next_node must be a Node object')

        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list
    """

    def __init__(self):
        """Initializes the SingleLinkedList object
        """
        self.__head = None

    def __str__(self):
        """Returns string for a SingleLinkedList instance
        """
        node = self.__head
        string = ""

        while node is not None:
            string += str(node.data)
            if node.next_node is not None:
                string += "\n"
            node = node.next_node

        return string

    def sorted_insert(self, value):
        """ inserts a new Node into the correct sorted position in the list
        (increasing order)
        """
        current = self.__head

        while current is not None and current.data < value:
            prev = current
            current = current.next_node

        node = Node(value, current)

        if current is self.__head:
            # current still points to head
            self.__head = node
        else:
            prev.next_node = node
