from collections import deque

class FIFOCache:
    def __init__(self, capacity):
        self.capacity = capacity          # Maximum number of items
        self.cache = {}                   # Stores key → value
        self.queue = deque()              # Tracks insertion order

    def get(self, key):
        """
        Return value if key exists, else -1
        """
        if key not in self.cache:
            return -1
        return self.cache[key]

    def put(self, key, value):
        """
        Insert key-value pair.
        If capacity exceeded, remove oldest item.
        """
        if key in self.cache:
            return

        if len(self.cache) >= self.capacity:
            oldest_key = self.queue.popleft()
            del self.cache[oldest_key]

        self.cache[key] = value
        self.queue.append(key)
