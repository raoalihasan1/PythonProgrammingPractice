from DataStructures import DataStructure
from Nodes import Node


class LinkedList(DataStructure):

    def __init__(self):
        self.__head = Node()
        self.__size = 0

    def count(self):
        return self.__size

    def add(self, val):
        current_node = self.__head
        if (current_node.get_value() is None):
            current_node.set_value(val)
        else:
            previous_node = current_node
            while current_node is not None:
                previous_node = current_node
                if current_node.get_value() == val:
                    return
                current_node = current_node.get_next_node()
            new_node = Node(val)
            previous_node.set_next_node(new_node)
            new_node.set_previous_node(previous_node)
        self.__size += 1

    def remove(self, val):
        current_node = self.__head
        previous_node = current_node
        while current_node is not None:
            if current_node.get_value() == val:
                if (current_node.get_previous_node() is None):
                    self.__head = current_node.get_next_node()
                else:
                    previous_node.set_next_node(current_node.get_next_node())
                    if (current_node.get_next_node() is not None):
                        current_node.get_next_node().set_previous_node(current_node.get_previous_node())
                self.__size -= 1
                return
            previous_node = current_node
            current_node = current_node.get_next_node()

    def peek(self):
        return self.__head.get_value()

    def show(self):
        current_node = self.__head
        while current_node is not None:
            if current_node.get_value() is not None:
                print(current_node.get_value(), end=" <-> ")
            current_node = current_node.get_next_node()
        print("None")

    def is_empty(self):
        return True if self.__size == 0 else False

    def _resize(self):
        pass
