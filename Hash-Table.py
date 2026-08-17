class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, key: str):
        mylist = []
        for char in key:
            mylist.append(ord(char))
        return sum(mylist)

    def add(self, key, value):
        calhash = self.hash(key)
        if calhash in self.collection.keys():
            self.collection[calhash].update({key: value})
            self.collection.update({self.hash(key): self.collection[calhash]})
        else:
            indict = {key: value}
            self.collection.update({self.hash(key): indict})

    def lookup(self, key):
        calhash = self.hash(key)
        if calhash in self.collection.keys() and key in self.collection[calhash].keys():
            return self.collection[calhash][key]
        return None

    def remove(self, key):
        calhash = self.hash(key)
        if calhash in self.collection.keys():
            return self.collection[calhash].pop(key, None)
        return None











