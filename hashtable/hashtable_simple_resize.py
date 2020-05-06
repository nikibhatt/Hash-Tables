class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.hash_table = [None] * self.capacity

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for x in key:
            hash = ((hash << 5) + hash) + ord(x)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        index = self.hash_index(key)
        n = HashTableEntry(key, value)
        if self.hash_table[index] is None:
            self.hash_table[index] = n
            return
        head = self.hash_table[index]
        cur = head
        while cur is not None:
            if cur.key == key:
                cur.value = value
                return
            cur = cur.next
        n.next = head
        self.hash_table[index] = n


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        if self.hash_table[index] is None:
            return

        head = self.hash_table[index]
        if head.key == key:
            head = head.next
            self.hash_table[index] = head
            return

        cur = head
        while cur.next is not None:
                prev = cur
                cur = cur.next
                if cur.key == key:
                    prev.next = cur.next
                    return
        return

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        head = self.hash_table[index]
        cur = head
        while cur is not None:
            if cur.key == key:
                return cur.value
            cur = cur.next
        return None

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        new_hash_table = [None] * 2 * self.capacity
        for i in range(len(self.hash_table)):
            if self.hash_table[i] is not None:
                new_index = self.hash_index(self.hash_table[i].key)
                new_hash_table[new_index] = self.hash_table[i]
        self.hash_table = new_hash_table

if __name__ == "__main__":
        ht = HashTable(8)

        ht.put("key-0", "val-0")
        ht.put("key-1", "val-1")
        ht.put("key-2", "val-2")
        ht.put("key-3", "val-3")
        ht.put("key-4", "val-4")
        ht.put("key-5", "val-5")
        ht.put("key-6", "val-6")
        ht.put("key-7", "val-7")
        ht.put("key-8", "val-8")
        ht.put("key-9", "val-9")

        print(ht.get("key-0"))
        print(ht.get("key-1"))
        print(ht.get("key-2"))
        print(ht.get("key-3"))
        print(ht.get("key-4"))
        print(ht.get("key-5"))
        print(ht.get("key-6"))
        print(ht.get("key-7"))
        print(ht.get("key-8"))
        print(ht.get("key-9"))
