import sys
import requests
import json
import matplotlib.pyplot as plt
from models import Student, GraduateStudent
from custom_utils import save_to_csv, load_from_csv

def fetch_advisor():
    