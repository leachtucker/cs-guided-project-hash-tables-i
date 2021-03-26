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
class LinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashTable:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.storage = [None] * self.capacity
        self.size = 0

    def get_load_factor(self):
        return self.size / self.capacity

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

    # put updates a value if it exists or
    def put(self, key, value):
        index = self.hash_index(key)
        new_node = LinkedListNode(key, value)

        if self.storage[index] is None:
            self.storage[index] = new_node
            self.size += 1
        else:
            current_head = self.storage[index]

            currNode = current_head
            while currNode is not None:
                if currNode.key == key:
                    # If we find an existing node with the given key, update that node's value
                    currNode.value = value
                    break

                currNode = currNode.next
            else:
                # if we go through this loop without breaking (we didn't find a node with that key), let's make the new_node the new head
                new_node.next = current_head
                self.storage[index] = new_node

                self.size += 1

        # After inserting a new node, we need to check if our load factor has hit the threshold of 0.7...if so, resize the storage
        if self.get_load_factor() >= 0.7:
            self.resize()

    def resize(self):
        current_storage = self.storage

        # Update
        self.capacity *= 2
        self.storage = [None] * self.capacity
        self.size = 0

        for bucket in current_storage:
            if bucket is None:
                continue

            head = bucket

            currNode = head
            while currNode is not None:
                self.put(currNode.key, currNode.value)

                currNode = currNode.next

    # Returns the value associated with a key
    def get(self, key):
        index = self.hash_index(key)

        # Return -1 for not found if we have nothing in storage at that index
        if self.storage[index] is None:
            return -1

        # Grab the head of the linked list and search over it until we find a node with the corresponding key
        head  = self.storage[index]

        currNode = head
        while currNode is not None:
            if currNode.key == key:
                return currNode.value

            # Update currNode to the next node
            currNode = currNode.next
        else:
            # if we get to the end of this loop without returning, let's return -1 for 'Not found'
            return -1

    def remove(self, key):
        index = self.hash_index(key)

        if self.storage[index] is None:
            return -1

        # Grab the head of the linked list and search over it until we find a node with the corresponding key
        head  = self.storage[index]

        currNode = head
        prevNode = None
        while currNode is not None:
            if currNode.key == key:
                if prevNode is None and currNode.next is None:
                    self.storage[index] = None
                elif prevNode is None:
                    self.storage[index] = currNode.next
                else:
                    prevNode.next = prevNode.next.next

                self.size -= 1
                break

            # Update currNode to the next node and prevNode to the node we just visited
            prevNode = currNode
            currNode = currNode.next

myTable = MyHashTable(8)
myTable.put('a', '1')
myTable.put('b', '2')

print(myTable.get('a'))
print(myTable.get('c'))

print(f'Size: {myTable.size}')

myTable.put('b', '1')

print(myTable.get('b'))

myTable.remove('b')

print(myTable.get('b'))

print(f'Size: {myTable.size}')

print('\n')


myTable.put('apple', '4')
print(f'Load factor: {myTable.get_load_factor()}')

myTable.put('peach', '7')
print(f'Load factor: {myTable.get_load_factor()}')

myTable.put('banana', '9')
print(f'Load factor: {myTable.get_load_factor()}')

myTable.put('cucumber', '11')
print(f'Load factor: {myTable.get_load_factor()}')

myTable.put('watermelon', '14')
print(f'Load factor: {myTable.get_load_factor()}')


print(f'Size: {myTable.size}')