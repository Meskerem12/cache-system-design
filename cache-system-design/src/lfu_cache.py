class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.freq = {}
        self.order = {}
        self.time = 0

    def get(self, key: str):
        if key not in self.cache:
            return -1
        self.freq[key] += 1
        return self.cache[key]

    def put(self, key: str, value):
        if self.capacity == 0:
            return

        self.time += 1

        if key in self.cache:
            self.cache[key] = value
            self.freq[key] += 1
            return

        if len(self.cache) >= self.capacity:
            min_freq = min(self.freq.values())
            candidates = [k for k in self.freq if self.freq[k] == min_freq]
            oldest = min(candidates, key=lambda k: self.order[k])
            del self.cache[oldest]
            del self.freq[oldest]
            del self.order[oldest]

        self.cache[key] = value
        self.freq[key] = 1
        self.order[key] = self.time
