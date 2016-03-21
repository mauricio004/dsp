# -*- coding: utf-8 -*-
# The football.csv file contains the results from the English Premier League.
# The columns labeled 'Goals' and 'Goals Allowed' contain the total number of
# goals scored for and against each team in that season (so Arsenal scored 79 goals
# against opponents, and had 36 goals scored against them). Write a program to read the file,
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.

# Team,Games,Wins,Losses,Draws,Goals,Goals Allowed,Points
import csv


def get_team_with_smallest_diff(data):
    smallest_difference = None
    team = None

    # Read data using DictReader
    try:
        with open(data, 'rb') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Calculate team difference.  Goals allowed might be higher than Goals. Return absolute value
                team_difference = abs(int(row['Goals']) - int(row['Goals Allowed']))
                if team_difference < smallest_difference or smallest_difference is None:
                    smallest_difference = team_difference
                    team = row['Team']
    except Exception as err:
        print 'Cannot read file: ' + str(err)

    return team






