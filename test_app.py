import pytest
from custom_utils import validate_email, validate_student_id
from models import Student, Course

def test_validate_student_id():
    assert validate_student_id("comp1234") == True
    assert validate_student_id("comp123") == False
    assert validate_student_id("1234comp") == False

def test_validate_email():
    assert validate_email("student@kent.ac.uk") == True
    assert validate_email("invalid@gmail.com") == False

def test_student_creation_and_validation():
    s = Student("Alice", "ECE", "test0000")
    assert s.name == "Alice"

    with pytest.raises(ValueError):
        s = Student("Bob", "ART", "test0000")

def test_course_addition():
    c1 = Course("Math", "M101")
    c2 = Course("Science", "S101")
    s1 = Student("Alice", "ECE", "test0000")
    
    c1.add_student(s1)
    c3 = c1 + c2
    assert s1 in c3.enrolled_students