import re
import csv
import os

def validate_student_id(student_id):
    pattern = r"^[a-zA-Z]{4}\d{4}$"
    return bool(re.search(pattern, student_id))

def validates_email(email):
    