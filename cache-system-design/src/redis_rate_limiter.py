import redis
import time
import csv
import os

class FixedWindowRateLimiter:
    def __init__(self, redis_host="localhost", redis_port=6379, max_requests=5, window=60):
        self.redis = redis.Redis(host=redis_host, port=redis_port, db=0)
        self.max_requests = max_requests
        self.window = window

    def is_allowed(self, user_id):
        key = f"rate:{user_id}"
        current = self.redis.get(key)
        if current is None:
            self.redis.set(key, 1, ex=self.window)
            return True
        elif int(current) < self.max_requests:
            self.redis.incr(key)
            return True
        else:
            return False

def load_students(csv_path):
    students = {}
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            roll_no = row['Roll No.']
            students[roll_no] = row
    return students

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    CSV_PATH = os.path.join(BASE_DIR, "..", "data", "student_dataset.csv")
    students = load_students(CSV_PATH)

    limiter = FixedWindowRateLimiter(max_requests=3, window=10)

    user_id = input("Enter your user ID: ")

    while True:
        roll_no = input("\nEnter Roll No to fetch student (or 'exit' to quit): ")
        if roll_no.lower() == 'exit':
            break
        if not limiter.is_allowed(user_id):
            print("⚠️ Rate limit exceeded! Try again later.")
            continue
        student = students.get(roll_no)
        if student:
            print("Student found:")
            for k, v in student.items():
                print(f"{k}: {v}")
        else:
            print("❌ Student not found.")
