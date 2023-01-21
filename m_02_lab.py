"""
Filename: m_02_lab.py
Author: Bidhya Gautam
Date: 1/21/2023

This program takes student name and GPA to test if they qualify for Dean's Lists or the Honor Roll. 
Student with GPA 3.5>= goes to Dean's List
Student with GAPA >=3.25 goes to Honor Roll
"""
while True:
    last_name = input("Enter the student's last name (enter 'ZZZ' to quit): ")
    if last_name == 'ZZZ':
        break
    first_name = input("Enter the student's first name: ")
    gpa = float(input("Enter the student's GPA: "))
    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List.")
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll.")
    else:
        print(f"{first_name} {last_name} does not qualify for the Dean's List or Honor Roll.")