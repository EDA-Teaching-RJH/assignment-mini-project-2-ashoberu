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