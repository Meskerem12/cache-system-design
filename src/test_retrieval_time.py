import time
import os
from load_data import load_students
from lru_cache import LRUCache   # you can test FIFO/LFU as well

# Locate CSV file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "..", "data", "student_dataset.csv")

# Load dataset once
students = load_students(CSV_PATH)
keys = list(students.keys())

# Choose a key to test
test_key = keys[0]

# -------------------------------
# 1️⃣ NORMAL CSV RETRIEVAL
# -------------------------------
start_csv = time.perf_counter()

# Simulate reading from CSV every time
students_from_csv = load_students(CSV_PATH)
record_csv = students_from_csv[test_key]

end_csv = time.perf_counter()
csv_time = end_csv - start_csv

# -------------------------------
# 2️⃣ CACHE RETRIEVAL
# -------------------------------
cache = LRUCache(capacity=5)

# Put data into cache
cache.put(test_key, students[test_key])

start_cache = time.perf_counter()
record_cache = cache.get(test_key)
end_cache = time.perf_counter()

cache_time = end_cache - start_cache

# -------------------------------
# RESULTS
# -------------------------------
print("CSV Retrieval Time :", csv_time, "seconds")
print("Cache Retrieval Time:", cache_time, "seconds")
