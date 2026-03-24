import re
import csv
import os

def validate_student_id(student_id):
    pattern = r"^[a-zA-Z]{4}\d{4}$"
    return bool(re.search(pattern, student_id))

def validates_email(email):
    pattern = r"^\w+@\w.+\.(ac\.uk|gov\.uk|nhs\.net)$"
    return bool(re.search(pattern, email))

def save_to_csv(filename, data_list):
    if not data_list:
        return
    keys = data_list[0].keys()
    file_exists = os.path.isfile(filename)

    with open(filename, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        if not file_exists:
            writer.writeheader()
        writer.writerows(data_list)

def load_from_csv(filename):
    
