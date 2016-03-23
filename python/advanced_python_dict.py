# -*- coding: utf-8 -*-

from advanced_python_regex import read_data

import re


def faculty_info(data_dict):

    # Dictionary with tuple (first name, last name) as key and list with info as values
    faculty_dict = {}

    # Loop over each faculty member to get names and info
    for faculty in data_dict.values():
        # Create list with names
        name = faculty['name'].split()
        # Name has only one word or less
        if len(name) < 2:
            faculty_dict[(name[0])] = [faculty[' degree'], faculty[' title'], faculty[' email']]
        # Name has two words
        # Add tuple (First Name, Last Name) as key
        elif len(name) == 2:
            faculty_dict[(name[0], name[1])] = [faculty[' degree'], faculty[' title'], faculty[' email']]
        # Name has more than 2 words.
        else:
            # Find if faculty abbreviates first name e.g J. Richard Landis
            match_1 = re.search(r'^[a-zA-Z]\.?$', name[0])
            # Join first name and middle name
            if match_1:
                faculty_dict[(name[0] + ' ' + name[1], name[2])] = [faculty[' degree'], faculty[' title'],
                                                                    faculty[' email']]
            # Add tuple (first Name, Last Name) as key
            else:
                faculty_dict[(name[0], name[2])] = [faculty[' degree'], faculty[' title'], faculty[' email']]

    return faculty_dict


def faculty_info_sorted(faculty_dict):

    return sorted(faculty_dict.items(), key=lambda key: key[0][1])


d_data = read_data('faculty.csv')
faculty_d = faculty_info(d_data)
print faculty_info_sorted(faculty_d)