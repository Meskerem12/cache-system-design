import time
import os
from load_data import load_students
from fifo_cache import FIFOCache
from lru_cache import LRUCache
from lfu_cache import LFUCache

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "..", "data", "student_dataset.csv")
students = load_students(CSV_PATH)
keys = list(students.keys())

test_key = keys[0]

start_csv = time.perf_counter()
students_from_csv = load_students(CSV_PATH)
record_csv = students_from_csv[test_key]
csv_time = time.perf_counter() - start_csv

fifo_cache = FIFOCache(capacity=5)
lru_cache = LRUCache(capacity=5)
lfu_cache = LFUCache(capacity=5)

fifo_cache.put(test_key, students[test_key])
lru_cache.put(test_key, students[test_key])
lfu_cache.put(test_key, students[test_key])

start_fifo = time.perf_counter()
_ = fifo_cache.get(test_key)
fifo_time = time.perf_counter() - start_fifo

start_lru = time.perf_counter()
_ = lru_cache.get(test_key)
lru_time = time.perf_counter() - start_lru

start_lfu = time.perf_counter()
_ = lfu_cache.get(test_key)
lfu_time = time.perf_counter() - start_lfu

print("\n--- Retrieval Time Comparison ---")
print(f"CSV Retrieval Time   : {csv_time:.6f} seconds")
print(f"FIFO Cache Retrieval : {fifo_time:.6f} seconds")
print(f"LRU Cache Retrieval  : {lru_time:.6f} seconds")
print(f"LFU Cache Retrieval  : {lfu_time:.6f} seconds")
