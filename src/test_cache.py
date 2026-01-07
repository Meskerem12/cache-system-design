import os
import time
from load_data import load_students
from fifo_cache import FIFOCache
from lru_cache import LRUCache
from lfu_cache import LFUCache

# -------------------------------
# 1️⃣ Setup CSV path and load dataset
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "..", "data", "student_dataset.csv")

print("Loading CSV from:", CSV_PATH)
students = load_students(CSV_PATH)
keys = list(students.keys())  # List of all Roll Numbers

# -------------------------------
# 2️⃣ Initialize caches with fixed capacity
# -------------------------------
CACHE_CAPACITY = 3
fifo = FIFOCache(CACHE_CAPACITY)
lru = LRUCache(CACHE_CAPACITY)
lfu = LFUCache(CACHE_CAPACITY)

# -------------------------------
# 3️⃣ Define request sequence (simulate multiple requests)
# -------------------------------
request_sequence = [keys[0], keys[1], keys[2], keys[0], keys[3], keys[0], keys[1]]

# -------------------------------
# 4️⃣ Test caches and measure retrieval time
# -------------------------------
print("\n--- Cache Hit/Miss Simulation ---")
for roll_no in request_sequence:

    # ---------------- FIFO ----------------
    start = time.perf_counter()
    value = fifo.get(roll_no)
    fifo_time = time.perf_counter() - start

    if value == -1:
        print(f"FIFO Cache Miss for {roll_no} → loading from CSV ({fifo_time:.6f} s)")
        fifo.put(roll_no, students[roll_no])
    else:
        print(f"FIFO Cache Hit for {roll_no} ({fifo_time:.6f} s)")

    # ---------------- LRU ----------------
    start = time.perf_counter()
    value = lru.get(roll_no)
    lru_time = time.perf_counter() - start

    if value == -1:
        print(f"LRU Cache Miss for {roll_no} → loading from CSV ({lru_time:.6f} s)")
        lru.put(roll_no, students[roll_no])
    else:
        print(f"LRU Cache Hit for {roll_no} ({lru_time:.6f} s)")

    # ---------------- LFU ----------------
    start = time.perf_counter()
    value = lfu.get(roll_no)
    lfu_time = time.perf_counter() - start

    if value == -1:
        print(f"LFU Cache Miss for {roll_no} → loading from CSV ({lfu_time:.6f} s)")
        lfu.put(roll_no, students[roll_no])
    else:
        print(f"LFU Cache Hit for {roll_no} ({lfu_time:.6f} s)")

# -------------------------------
# 5️⃣ Compare single retrieval from CSV (without cache)
# -------------------------------
test_key = keys[0]
start_csv = time.perf_counter()
record_csv = load_students(CSV_PATH)[test_key]
csv_time = time.perf_counter() - start_csv

# Measure retrieval time from cache
start = time.perf_counter()
record_fifo = fifo.get(test_key)
fifo_time = time.perf_counter() - start

start = time.perf_counter()
record_lru = lru.get(test_key)
lru_time = time.perf_counter() - start

start = time.perf_counter()
record_lfu = lfu.get(test_key)
lfu_time = time.perf_counter() - start

print("\n--- Retrieval Time Comparison ---")
print(f"CSV Retrieval Time for {test_key}: {csv_time:.6f} seconds")
print(f"FIFO Cache Retrieval Time for {test_key}: {fifo_time:.6f} seconds")
print(f"LRU Cache Retrieval Time for {test_key}: {lru_time:.6f} seconds")
print(f"LFU Cache Retrieval Time for {test_key}: {lfu_time:.6f} seconds")

# -------------------------------
# 6️⃣ Print final cache states
# -------------------------------
print("\n--- Final Cache States ---")
print("FIFO cache keys:", list(fifo.queue))
print("LRU cache keys:", list(lru.cache.keys()))
print("LFU cache keys:", list(lfu.cache.keys()))

print("FIFO current cache:", list(fifo.queue))
print("LRU current cache:", list(lru.cache.keys()))
print("LFU current cache:", list(lfu.cache.keys()))
