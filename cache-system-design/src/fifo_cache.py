from collections import deque

class FIFOCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.queue = deque()

    def get(self, key: str):
        if key not in self.cache:
            return -1
        return self.cache[key]

    def put(self, key: str, value):
        if key in self.cache:
            return
        if len(self.cache) >= self.capacity:
            oldest_key = self.queue.popleft()
            del self.cache[oldest_key]
        self.cache[key] = value
        self.queue.append(key)
