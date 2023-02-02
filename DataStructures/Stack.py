from DataStructures import DataStructure


class Stack(DataStructure):

    def __init__(self):
        self.__struct = [None]*1000
        self.__front_pointer = -1
        self.__size = 0
        self.__stack_size = 1000

    def show(self):
        clean_stack = [x for x in self.__struct if x is not None]
        print()
        for x in range(len(clean_stack) - 1, -1, -1):
            if (x == self.__front_pointer):
                print(f"{x}: {clean_stack[x]} <= Front Pointer")
            else:
                print(f"{x}: {clean_stack[x]}")
        print()

    def add(self, val):
        self.__front_pointer += 1
        self.__struct[self.__front_pointer] = val
        self.__size += 1
        if (self.__size == self.__stack_size):
            self._resize()

    def remove(self):
        if (self.__size == 0):
            return None
        val = self.__struct[self.__front_pointer]
        self.__struct[self.__front_pointer] = None
        self.__front_pointer -= 1
        self.__size -= 1
        return val

    def peek(self):
        return self.__struct[self.__front_pointer]

    def is_empty(self):
        if (self.__stack_size == len([x for x in self.__struct if x is None])):
            return True
        return False

    def count(self):
        return self.__size

    def _resize(self):
        tmp_struct = [x for x in self.__struct if x is not None]
        self.__stack_size *= 2
        self.__struct = [None]*self.__stack_size
        for x in range(len(tmp_struct)):
            self.__struct[x] = tmp_struct[x]
        self.__front_pointer = len(tmp_struct) - 1
