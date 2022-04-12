from Memory import Memory

class CyclicCache(Memory):

    def name(self):
        return "Cyclic"

    def __init__(self, data, size=4):
        super().__init__(data)
        self.cache_count = 1
        self.cache1loc, self.cache1val = "", ""
        self.cache2loc, self.cache2val = "", ""
        self.cache3loc, self.cache3val = "", ""
        self.cache4loc, self.cache4val = "", ""

    def lookup(self, location):
        if(location == self.cache1loc):
            return self.cache1val
        elif(location == self.cache2loc):
            return self.cache2val
        elif(location == self.cache3loc):
            return self.cache3val
        elif(location == self.cache4loc):
            return self.cache4val
        else:
            value = super().lookup(location)
            if(self.cache_count == 1):
                self.cache1loc = location
                self.cache1val = value
                self.cache_count += 1
            elif(self.cache_count == 2):
                self.cache2loc = location
                self.cache2val = value
                self.cache_count += 1
            elif(self.cache_count == 3):
                self.cache3loc = location
                self.cache3val = value
                self.cache_count += 1
            else:
                self.cache4loc = location
                self.cache4val = value
                self.cache_count = 1
            return value

class LRUCache(Memory):
    
    def name(self):
        return "LRU"

    def __init__(self, data, size=4):
        super().__init__(data)
        self.least_recently_used_pos = 1
        self.cache1loc, self.cache1val = "", ""
        self.cache2loc, self.cache2val = "", ""
        self.cache3loc, self.cache3val = "", ""
        self.cache4loc, self.cache4val = "", ""

    def lookup(self, location):
        if(location == self.cache1loc):
            self.least_recently_used_pos = 2
            return self.cache1val
        elif(location == self.cache2loc):
            self.least_recently_used_pos = 3
            return self.cache2val
        elif(location == self.cache3loc):
            self.least_recently_used_pos = 4
            return self.cache3val
        elif(location == self.cache4loc):
            self.least_recently_used_pos = 1
            return self.cache4val
        else:
            value = super().lookup(location)
            if(self.least_recently_used_pos == 1):
                self.cache1loc = location
                self.cache1val = value
                self.least_recently_used_pos = 2
            elif(self.least_recently_used_pos == 2):
                self.cache2loc = location
                self.cache2val = value
                self.least_recently_used_pos = 3
            elif(self.least_recently_used_pos == 3):
                self.cache3loc = location
                self.cache3val = value
                self.least_recently_used_pos = 4
            elif(self.least_recently_used_pos == 4):
                self.cache4loc = location
                self.cache4val = value
                self.least_recently_used_pos = 1
            return value

                       