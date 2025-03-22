# hash table


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def print(self):
        return self.table

    def hash_function(self, key):
        """
        Summary : We can use hash function in many ways
        Args:
            self - Class object
            key  - Data or any value
        """

        # At first do the hash for key and divide by size
        # We will get some int value then use it as index
        print(f"Generated hash value for key {key}: {hash(key)%self.size}")
        return hash(key) % self.size

    def insert(self, key, value):
        """
        collions: usually collision happens when two or more different keys have same index or hash value
        There is a chance of collion in hashing so to handle those
        we can have the concepts like
        1. Chaining
        2. Probing
            - Linear Probing(Look for immediate next index to store)
            - Quadratic Probing ( Use another hash to store the key)
        """
        index = self.hash_function(key)
        # Chaning
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self.hash_function(key)
        for item in self.table[index]:
            if item[0] == key:
                print("Value found ", end="")
                return item[1]
        print("key not found")
        return None  # Key not found

    def remove(self, key):
        """
        Summary : To remove elements from hash table using enumerate 
        because the for a single index there can be multple key value pairs 
        so we need to add a counter if you want to remove from the table
        """
        index = self.hash_function(key)
        for i, item in enumerate(self.table[index]):
            print("enumerate function creates counter :", i)
            if item[0] == key:
                del self.table[index][i]
                return True
        return False


if __name__ == "__main__":
    # Create a hash table with size 5
    ht = HashTable(5)

    # Insert some key-value pairs
    ht.insert("apple", 10)
    ht.insert("banana", 20)
    ht.insert("grape", 30)
    ht.insert("kiwi", 40)

    # Insert a key that causes a collision
    ht.insert("plum", 50)

    # displat hash table
    print(ht.print())

    # Retrieve values
    print(ht.get("banana"))  # Output: 20
    print(ht.get("grape"))  # Output: 30

    # Remove a key
    ht.remove("kiwi")
    print(ht.get("kiwi"))  # Output: None (kiwi has been removed)
