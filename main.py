import sys
import requests
import json
import matplotlib.pyplot as plt
from models import Student, GraduateStudent
from custom_utils import save_to_csv, load_from_csv

def fetch_advisor():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/users/1")
        if response.status_code == 200:
            return json.loads(response.text)["name"]
    except Exception:
        pass
    return "TBD"

def plot_degree_distribution(students_data):
    