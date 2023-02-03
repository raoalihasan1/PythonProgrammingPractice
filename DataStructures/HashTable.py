from DataStructures import DataStructure
from Nodes import Node


class HashTable(DataStructure):

    def __init__(self):
        self.__hash_table_size = self.next_prime(10)
        self.__struct = [Node() for x in range(self.__hash_table_size)]
        self.__size = 0

    def is_prime(self, n):
        i = 2
        while (i ** 2 <= n):
            if (n % i == 0):
                return False
            i += 1
        return True

    def next_prime(self, n):
        while (not self.is_prime(n)):
            n += 1
        return n

    def hash_func(self, val):
        sum = 0
        if (isinstance(val, int) or isinstance(val, float)):
            sum = val
        elif (isinstance(val, str)):
            index = 0
            for char in val:
                sum += (index + len(val)) ** ord(char)
                index += 1
        if (val == "Lahore"):
            print(sum % self.__hash_table_size)
        return sum % self.__hash_table_size

    def show(self):
        print()
        for x in range(self.__hash_table_size):
            current_node = self.__struct[x]
            if (current_node.get_value() is None):
                continue
            else:
                print(f"{x}:", end=" ")
                while current_node is not None:
                    if (current_node.get_value() is not None):
                        print(current_node.get_value(), end=" <-> ")
                    current_node = current_node.get_next_node()
                print("None")
            print()

    def find(self, val):
        current_node = self.__struct[self.hash_func(val)]
        while current_node is not None and current_node.get_value() != val:
            current_node = current_node.get_next_node()
        if current_node is not None:
            return True
        return False

    def add(self, val):
        if (not self.find(val)):
            current_node = self.__struct[self.hash_func(val)]
            if (current_node.get_value() is None):
                current_node.set_value(val)
            else:
                previous_node = current_node
                while current_node is not None:
                    previous_node = current_node
                    current_node = current_node.get_next_node()
                new_node = Node(val)
                previous_node.set_next_node(new_node)
                new_node.set_previous_node(previous_node)
            self.__size += 1
            if (self.__size / self.__hash_table_size >= 0.65):
                self._resize()

    def remove(self, val):
        if (self.find(val)):
            self.__size -= 1
            current_node = self.__struct[self.hash_func(val)]
            previous_node = current_node
            while current_node is not None and current_node.get_value() != val:
                previous_node = current_node
                current_node = current_node.get_next_node()
            if (current_node.get_previous_node() is not None):
                if (current_node.get_next_node() is not None):
                    previous_node.set_next_node(current_node.get_next_node())
                    current_node.get_next_node().set_previous_node(current_node.get_previous_node())
                else:
                    current_node.get_previous_node().set_next_node(Node())
            else:
                self.__struct[self.hash_func(val)] = Node()

    def peek(self):
        pass

    def is_empty(self):
        if (self.__size == 0):
            return True
        return False

    def count(self):
        return self.__size

    def _resize(self):
        tmp_struct = [x for x in self.__struct if x is not None]
        self.__size = 0
        self.__hash_table_size = self.next_prime(self.__hash_table_size * 2)
        self.__struct = [Node() for x in range(self.__hash_table_size)]
        for x in range(len(tmp_struct)):
            current_node = tmp_struct[x]
            while current_node is not None:
                self.add(current_node.get_value())
                current_node = current_node.get_next_node()
