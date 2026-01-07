import csv

def load_students(csv_path):
    """
    Loads student data from CSV file.
    Uses Roll No. as key.
    Returns a dictionary: {roll_no: student_record}
    """
    students = {}

    with open(csv_path, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            roll_no = row["Roll No."]
            students[roll_no] = row

    return students
