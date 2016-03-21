# -*- coding: utf-8 -*-

import csv
import re


def read_data(data):
    # Store all data in dictionary
    faculty_dict = {}

    # Read data using DictReader function
    try:
        with open(data, 'rb') as f:
            reader = csv.DictReader(f)
            for row in reader:
                faculty_dict[row['name']] = row
    except Exception as err:
        print 'Cannot read file', + str(err)

    return faculty_dict


def get_different_degrees(data_dict):
    # List with all degrees
    all_degrees_lst = []

    # Dictionary with degree as key and frequency as value
    degrees_freq = {}

    # Loop over each faculty member
    for faculty in data_dict.values():
        # List of degree or degrees
        degrees = clean_text(faculty[' degree'])
        # Check if faculty has more than one degree
        if len(degrees) > 1:
            for d in degrees:
                all_degrees_lst.append(d)
        else:
            all_degrees_lst.append(degrees[0])

    # Add degrees to dictionary and add frequency
    for a_d in all_degrees_lst:
        degrees_freq.setdefault(a_d, 0)
        degrees_freq[a_d] += 1

    return degrees_freq


def clean_text(txt):
    # List for title (len = 1) or multiple titles
    title_lst = []

    # Split when multiple titles
    words = txt.split()

    # Convert to uppercase and remove dots
    for word in words:
        if word != '':
            word = word.upper()
            word = word.replace('.', '')
            title_lst.append(word)

    return title_lst


def get_different_titles(data_dict):
    # List with all titles
    all_titles_lst = []

    # Loop over data_dict
    for v in data_dict.values():
        print v



data_d = read_data('faculty.csv')
# print get_different_degrees(data_d)
print get_different_titles(data_d)