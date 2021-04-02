from linked_list import Node, LinkedList
from blossom_lib import flower_definitions


class HashMap:
    def __init__(self, size):
        self.array_size = size
        self.array = [LinkedList() for x in range(self.array_size)]

    def hash(self, key):
        return sum(key.encode())

    def compress(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        array_index = self.compress(self.hash(key))
        payload = Node([key, value])
        list_at_array = self.array[array_index]
        for n in list_at_array:
            if n[0] == key:
                n[1] = value
                return
        list_at_array.insert(payload)

    def retrieve(self, key):
        array_index = self.compress(self.hash(key))
        list_at_index = self.array[array_index]
        for n in list_at_index:
            if n[0] == key:
                return n[1]
        return None

    def list(self):
        for i in self.array:
            for n in i:
                print(self.array.index(i), n[0], n[1])


blossom = HashMap(len(flower_definitions))
for i in flower_definitions:
    blossom.assign(i[0], i[1])
    #print(i[0], i[1])

for i in flower_definitions:
    print(i[0], i[1], blossom.retrieve(i[0]))

blossom.list()
