# -*- coding: utf-8 -*-

import csv

# Question 5
def write_data(email_list, file_name):
    """
    This function writes data from a list to a .csv file
    :param email_list: a list with email addresses
    :param file_name: a string with the name of the .csv file
    :return:
    """
    # Write to file_name and read from email_list
    try:
        with open(file_name, 'w') as f_write:
            writer = csv.writer(f_write, delimiter=',')
            for email in email_list:
                writer.writerow([email])
    except Exception as err:
        print 'Cannot write to file: ' + str(err)

