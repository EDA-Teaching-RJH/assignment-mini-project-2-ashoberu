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
    
