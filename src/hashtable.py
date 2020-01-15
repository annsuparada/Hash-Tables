# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.size = 0

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.

        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # index = self._hash_mod(key) #compute index of key
        # # self.size += 1 #increment size
        
        # node = self.storage[index]
        # #check if node is empty
        # if node is None:
        #     self.storage[index] = LinkedPair(key, value)
        #     return
        
        # while node.next:
        #     node = node.next
        # node.next = LinkedPair(key, value)  
        index = self._hash_mod(key)
        current_pair = self.storage[index]
        last_pair = None
        while current_pair is not None and current_pair.key is not key:
            last_pair = current_pair
            current_pair = last_pair.next
        if current_pair is not None:
            current_pair.value = value
        else:
            new_pair = LinkedPair(key, value)
            new_pair.next = self.storage[index]
            self.storage[index] = new_pair



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] is None:
            #Print a warning if the key is not found.
            print(f'Error, key is not found in index {index}')
            return
        
        pair = self.storage[index]
        searching = True
        while pair is not None and searching is True:
            if pair.key == key:
                self.storage[index] = None
                searching = False
            else:
                pair = pair.next


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        node = self.storage[index]
        while node is not None:
            if node.key == key:
                return node.value
            node = node.next

        return None  


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2

        new_storage = [None] * self.capacity
        copy = self.storage
        self.storage = new_storage
        for pair in copy:
            current_pair = pair
            while current_pair is not None:
                self.insert(current_pair.key, current_pair.value)
                current_pair = current_pair.next

        


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")
    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")


