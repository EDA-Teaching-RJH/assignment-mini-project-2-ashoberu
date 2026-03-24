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
    if not students_data:
        print("No data to plot.")
        return
        
    degrees = {}
    for s in students_data:
        deg = s.get("degree")
        degrees[deg] = degrees.get(deg, 0) + 1

    plt.figure(figsize=(8, 5))
    plt.bar(degrees.keys(), degrees.values(), color='skyblue')
    plt.title('Student Enrollment by Degree')
    plt.xlabel('Degree Program')
    plt.ylabel('Number of Students')
    plt.show()

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <AdminName>")
        sys.exit(1)
    
    admin_name = sys.argv[1]
    print(f"\n--- Welcome to the University Manager, {admin_name}! ---")

    s1 = Student("Alice Smith", "ECE", "abcd1234")
    s2 = GraduateStudent("Bob Jones", "BIO", "efgh5678", "Cellular Biology")
    s3 = Student("Charlie Day", "ECE", "ijkl9012")

    save_to_csv("students.csv", [s1.to_dict(), s2.to_dict(), s3.to_dict()])
    loaded_data = load_from_csv("students.csv")
    print(f"-> Loaded {len(loaded_data)} students from CSV.")

    print(f"-> Assigned Advisor: {fetch_advisor()}")

    print("-> Generating enrollment chart...")
    plot_degree_distribution(loaded_data)
    

