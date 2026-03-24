from custom_utils import validate_student_id

class Student:
    VALID_DEGREES = ["ECE", "BIO", "MECH", "EEE"]

    def __init__(self, name, degree, student_id):
        if not name:
            raise ValueError("Name cannot be empty.")
        if not validate_student_id(student_id):
            raise ValueError("Invalid Student ID format.")
        
        self.name = name
        self.student_id = student_id
        self._degree = None
        self.degree = degree
    
    @property
    def degree(self):
        return self._degree
    
    @degree.setter
    def degree(self, value):
        if value not in self.VALID_DEGREES:
            raise ValueError(f"Degree must be one of {self.VALID_DEGREES}")
        self._degree = value

    def to_dict(self):
        return{"name": self.name, "student_id": self.student_id, "degree": self.degree, "type": "Student", "extra": ""}
    
class GraduateStudent(Student):
    def __init__(self, name, degree, student_id, research_topic):
        super().__init__(name, degree, student_id)
        self.research_topic = research_topic

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "Graduate"
        data["extra"] = self.research_topic
        return data
    
class Course:
    def __init__(self, course_name, course_code):
        self.course_name = course_name
        self.course_code = course_code
        self.enrolled_students = []

    def add_student(self, student):
        if student not in self.enrolled_students:
            self.enrolled_students.append(student)
    
    def __add__(self, other):
        new_course = Course(f"{self.course_name} & {other.course_name}", "COMBINED")
        for student in self.enrolled_students + other.enrolled_students:
            new_course.add_student(student)
        return new_course