import pytest
from custom_utils import validate_email, validate_student_id
from models import Student, Course

def test_validate_student_id():
    