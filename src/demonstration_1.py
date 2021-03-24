"""
Your task is create your own HashTable without using a built-in library.

Your HashTable needs to have the following functions:

- put(key, value) : Inserts a (key, value) pair into the HashTable. If the
value already exists in the HashTable, update the value.
- get(key): Returns the value to which the specified key is mapped, or -1 if
this map contains no mapping for the key.
- remove(key) : Remove the mapping for the value key if this map contains the
mapping for the key.

Example:

```plaintext
hash_table = MyHashTable();
hash_table.put("a", 1);
hash_table.put("b", 2);
hash_table.get("a");            // returns 1
hash_table.get("c");            // returns -1 (not found)
hash_table.put("b", 1);         // update the existing value
hash_table.get("b");            // returns 1
hash_table.remove("b");         // remove the mapping for 2
hash_table.get("b");            // returns -1 (not found)
```
"""
class MyHashTable:
    def __init__(self, capacity):
        self.storage = [None] * capacity
        self.capacity = capacity
        self.occupied = 0

    def hash(self, key):
        # DJB2 HASH
        str_key = str(key).encode()

        hash_value = 5381

        # Bit-shift
        for b in str_key:
            hash_value = ((hash_value << 5) + hash_value) + b
            hash_value &= 0xffffffff

        return hash_value

    def hash_index(self, key):
        # Return an integer index within the boundaries of the underlying storage (list)
        return self.hash(key) % self.capacity

    def put(self, key, value):
        index = self.hash_index(key)
        self.storage[index] = value
        return index


    def get(self, key):
        index = self.hash_index(key)
        return self.storage[index]


    def remove(self, key):
        index = self.hash_index(key)
        self.storage[index] = None

        return self.storage[index]


myTable = MyHashTable(36)
myTable.put('apple', 'fruit')
myTable.put('cucumber', 'vegetable')
myTable.put('broccoli', 'vegetable')

print(myTable.get('apple'))
print(myTable.get('cucumber'))
print(myTable.get('broccoli'))
print('\n')

myTable.remove('apple')
print(myTable.get('apple'))
