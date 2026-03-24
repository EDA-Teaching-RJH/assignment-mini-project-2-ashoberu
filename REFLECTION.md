Connection to Course Materials
This application serves as a comprehensive demonstration of the concepts I covered in Workshops 7 through 9:

Workshop 7 (Libraries & Arguments):
I used sys.argv in main.py to require an admin name when running the script, so it won’t execute without the correct argument. I also used external libraries like requests and json to fetch dummy adviser data from an API, and matplotlib to visualise student enrolment.

Workshop 8 (Regex, Testing, File I/O):
I created a modular custom_utils.py file that uses re.search to enforce strict formats for emails and student IDs. I used csv.DictWriter and csv.DictReader to save and load student data. I also built a test suite (test_app.py) with pytest to check validation functions and object creation, including edge cases like raising ValueError.

Workshop 9 (OOP):
In models.py, I built a class hierarchy using inheritance (GraduateStudent from Student). I used @property for encapsulation and validation of the degree attribute, and implemented operator overloading (__add__) in the Course class to combine course rosters.

Development Process:
The main challenge was making sure the OOP structure worked smoothly with the File I/O system. By adding a to_dict() method in the Student superclass, I could easily convert object instances into a format that csv.DictWriter can use to write to students.csv. Structuring the application in a modular way (separating utilities, models, and main logic) also made unit testing much easier.