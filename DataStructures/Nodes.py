class Node:

    def __init__(self, val=None, previous=None, next=None):
        self.__val = val
        self.__previous_node = previous
        self.__next_node = next

    def get_value(self):
        return self.__val

    def get_previous_node(self):
        return self.__previous_node

    def get_next_node(self):
        return self.__next_node

    def set_value(self, val):
        self.__val = val

    def set_previous_node(self, previous):
        self.__previous_node = previous

    def set_next_node(self, next):
        self.__next_node = next
