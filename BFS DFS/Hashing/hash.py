class Entity:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashMap:

    def __init__(self):
        self.entities = [None for _ in range(5)]

    def put(self, key, value):
        hashValue = abs(hash(key) % len(self.entities))
        self.entities[hashValue] = Entity(key, value)

    def get(self, key):
        hashValue = abs(hash(key) % len(self.entities))
        if self.entities[hashValue] != None and self.entities[hashValue].key == key:
            return self.entities[hashValue].value
        # if does not exist
        return None

    def remove(self, key):

        hashValue = abs(hash(key) % len(self.entities))
        if self.entities[hashValue] != None and self.entities[hashValue].key:
            self.entities[hashValue] = None



if __name__ == '__main__':
    map = HashMap()
    map.put('Apple', 'Fruit is sweet')
    map.put('Apple', 'collision occurred')
    print(map.get('Apple'))
    print(map.remove('Apple'))
    print(map.get('Apple'))
