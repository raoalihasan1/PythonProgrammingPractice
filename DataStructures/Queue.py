from DataStructures import DataStructure


class Queue(DataStructure):

    def __init__(self):
        self.__struct = [None]*1000
        self.__front_pointer = 0
        self.__rear_pointer = -1
        self.__size = 0
        self.__queue_size = 1000

    def show(self):
        print()
        print([x for x in self.__struct if x is not None])
        print(
            f"\nFront Pointer: {self.__struct[self.__front_pointer]}\nRear Pointer: {self.__struct[self.__rear_pointer]}\n")

    def add(self, val):
        self.__rear_pointer += 1
        self.__struct[self.__rear_pointer] = val
        self.__size += 1
        if (self.__size == self.__queue_size):
            self._resize()

    def remove(self):
        if (self.__size == 0):
            return None
        val = self.__struct[self.__front_pointer]
        self.__struct[self.__front_pointer] = None
        self.__front_pointer += 1
        self.__size -= 1
        return val

    def peek(self):
        return self.__struct[self.__front_pointer]

    def is_empty(self):
        if (self.__queue_size == len([x for x in self.__struct if x is None])):
            return True
        return False

    def count(self):
        return self.__size

    def _resize(self):
        tmp_struct = [x for x in self.__struct if x is not None]
        self.__queue_size *= 2
        self.__struct = [None]*self.__queue_size
        for x in range(len(tmp_struct)):
            self.__struct[x] = tmp_struct[x]
        self.__front_pointer = 0
        self.__rear_pointer = len(tmp_struct) - 1
