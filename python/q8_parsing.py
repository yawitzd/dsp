#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.


import csv

  def read_data(data):
    '''Returns 'fbd', a list of lists'''
    fb = open('football.csv')
    csv_fb = csv.reader(fb)
    fbd = [] 
    for row in csv_fb:
      fbd.append(row) 
    fb.close()
    return fbd

  def add_score_difference(parsed_data):
    '''Adds a column to the data for score difference'''
    d = parsed_data
    for i in range(len(d)):
      if i == 0:
        d[i].append('Score Difference')
      else:
        d[i].append(int(d[i][5]) - int(d[i][6]))
    return d
    
  
  def get_min_team(parsed_data):
    d = add_score_difference(parsed_data)
    diffs = []
    teams = []
    for row in d:
      if d.index(row) > 0:
        diffs.append(row[8])
        teams.append(row[0])
    i = diffs.index(min(diffs))
    return teams[i]
    

      
