#!/usr/bin/env python3

"""
File: students.py
Name:

Description:
Sources:
"""


def main():
    filename = "data.txt"
    students = {}

    populate_dicts(students, filename)
    add_letter_grades(students, letters_added)
    display_students(students)


# This will add the student data from the file into the dictinoary that was initiailzed in the main() function
def populate_dicts(students, filename):
    # Code here


# This will add the letter grades to the end of the dictionary keys
def add_letter_grades(students, letters_added):
    # Code here


# This will print all of the student data (names, IDs, grades)
def display_students(students):
    # Code here


if __name__ == "__main__":
    main()