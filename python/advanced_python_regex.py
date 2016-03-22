# -*- coding: utf-8 -*-

import csv
import re


def read_data(data):
    """
    This function reads a .csv file from disk with faculty data and store it in a dictionary.
    :param data: .csv file
    :return: a dictionary with faculty names as keys and a dictionary with faculty info as values.
    """
    # Store all data in dictionary
    faculty_dict = {}

    # Read data using DictReader function
    try:
        with open(data, 'rb') as f_read:
            reader = csv.DictReader(f_read)
            for row in reader:
                faculty_dict[row['name']] = row
    except Exception as err:
        print 'Cannot read file', + str(err)

    return faculty_dict

# Question 1
def get_different_degrees(data_dict):
    """
    This function reads a dictionary with faculty data.  It extracts and clean the degree for each faculty member.
    It also calculates the degree frequency for all the department.
    :param data_dict: a dictionary with faculty names as keys and faculty info as values.
    :return: a dictionary with all degrees as keys and their frequencies as values.
    """

    # List with all degrees
    all_degrees_lst = []

    # Dictionary with degree as key and frequency as value
    degrees_freq_dict = {}

    # Loop over each faculty member to get degrees
    for faculty in data_dict.values():
        # List of degree or degrees
        degrees = clean_text(faculty[' degree'])
        # Check if faculty has more than one degree
        if len(degrees) > 1:
            for d in degrees:
                all_degrees_lst.append(d)
        else:
            all_degrees_lst.append(degrees[0])

    # Add degrees to dictionary and compute frequency
    for degree in all_degrees_lst:
        degrees_freq_dict.setdefault(degree, 0)
        degrees_freq_dict[degree] += 1

    return degrees_freq_dict


def clean_text(txt):
    """
    This function split and clean a string
    :param txt: a string
    :return: a list with one or more strings
    """
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

# Question 2
def get_different_titles(data_dict):
    """
    This function reads a dictionary with faculty data.  It extracts the title for each faculty member.
    It also calculates the title frequency for all the department.
    :param data_dict: a dictionary with faculty names as keys and faculty info as values.
    :return: a dictionary with all titles as keys and their frequencies as values.
    """
    # List with all titles
    all_titles_lst = []

    # Dictionary with title as key and frequency as value
    titles_freq_dict = {}

    # Loop over data_dict to get titles
    for faculty in data_dict.values():
        # Add first word of title to list e.g. Associate
        all_titles_lst.append(faculty[' title'].split()[0])

    # Add titles to dictionary and compute frequency
    for title in all_titles_lst:
        titles_freq_dict.setdefault(title, 0)
        titles_freq_dict[title] += 1

    return titles_freq_dict

# Question 3
def get_email_addresses(data_dict):
    """
    This function reads a dictionary with faculty data.  It extracts the email for each faculty member.
    :param data_dict: a dictionary with faculty names as keys and faculty info as values.
    :return: a list with all emails
    """
    # List with all email addresses
    all_emails_lst = []

    # Loop over data_dict to get emails
    for faculty in data_dict.values():
        # Add email to list
        all_emails_lst.append(faculty[' email'])

    return all_emails_lst

# Question 4
def get_email_domains(all_emails_lst):
    """
    This function reads a list of emails and extract the domain for each email.
    :param all_emails_lst: a list with emails
    :return: a dictionary with email domains as keys and their frequencies as values.
    """
    # List with all email domains
    all_domains_lst = []

    # Dictionary with email domain as key and frequency as value
    domains_freq_dict = {}

    # Loop over emails list to get domains
    for email in all_emails_lst:
        email_domain_match = re.search(r'@([\w.]+)', email)
        if email_domain_match:
            all_domains_lst.append(email_domain_match.group(1))
        else:
            all_domains_lst.append('No Match')

    # Add domains to dictionary and compute frequencies
    for domain in all_domains_lst:
        domains_freq_dict.setdefault(domain, 0)
        domains_freq_dict[domain] += 1

    return domains_freq_dict
