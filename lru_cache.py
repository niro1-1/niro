# Adding LRU Cache Implementation

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}  # key: value
        self.capacity = capacity
        self.order = []  # to track the order of keys

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # Move the accessed key to the end of the order
        self.order.remove(key)
        self.order.append(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.order.remove(key)
        else:
            if len(self.cache) >= self.capacity:
                # Remove the least recently used item
                lru = self.order.pop(0)
                del self.cache[lru]
            self.cache[key] = value
        self.order.append(key)

# Example usage
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  # returns 1
cache.put(3, 3)  # evicts key 2
print(cache.get(2))  # returns -1 (not found)