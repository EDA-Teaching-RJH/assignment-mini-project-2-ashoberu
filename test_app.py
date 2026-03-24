import pytest
from custom_utils import validate_email, validate_student_id
from models import Student, Course

def test_validate_student_id():
    assert validate_student_id("comp1234") == True
    assert validate_student_id("comp123") == False
    assert validate_student_id("1234comp") == False

def test_validate_email():
    