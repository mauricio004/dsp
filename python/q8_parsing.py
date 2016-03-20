# -*- coding: utf-8 -*-
# The football.csv file contains the results from the English Premier League.
# The columns labeled 'Goals' and 'Goals Allowed' contain the total number of
# goals scored for and against each team in that season (so Arsenal scored 79 goals
# against opponents, and had 36 goals scored against them). Write a program to read the file,
# then print the name of the team with the smallest difference in \‘for\’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.


import csv

# Team,Games,Wins,Losses,Draws,Goals,Goals Allowed,Points


def get_team_with_smallest_diff_team(data):
    smallest_difference = None
    team = None


    try:
        with open(data, 'rb') as f:
            reader = csv.DictReader(f)
            for row in reader:
                team_difference = int(row['Goals']) - int(row['Goals Allowed'])

    except Exception as err:
        print 'Cannot read file: ' + str(err)



def read_data(data):
    dict_teams = {}
    try:
        with open(data, 'rb') as f:
            reader = csv.DictReader(f, delimiter=',')

            for row in reader:
                dict_teams[row['Team']] = row
    except Exception as err:
        print 'Cannot read file: ' + str(err)

    return dict_teams


def get_min_score_difference(parsed_data):
    # COMPLETE THIS FUNCTION
    return


def get_team(self, index_value, parsed_data):
    # COMPLETE THIS FUNCTION
    return


filename = '/Users/Mauricio/ds/metis/prework/dsp/python/football.csv'
# print get_min_score_difference(read_data(filename))
get_team_with_smallest_diff_team(filename)
