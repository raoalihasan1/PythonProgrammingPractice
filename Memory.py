class Memory:
    def __init__(self, data):
        self.memory = data
        self.memory_hit_count = 0

    def get_memory_hit_count(self):
        return self.memory_hit_count

    def name(self):
        return "Memory"

    def lookup(self, address):
        self.memory_hit_count += 1
        try:
            return self.memory[address]
        except IndexError as error:
            print("Error: Unknown Memory Location")
            return None
