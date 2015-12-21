import os, csv, re


def read_data(file):
  data = open(file)
  d = []
  csv_data = csv.reader(data)
  for row in csv_data:
    d.append(row)
  data.close()
  return d
  
def get_names(parsed_data):
  '''Returns a list of faculty names'''
  full = []
  for i in range(len(d)):
    if i > 0:
      full.append(d[i][0])
  return full
  
  

def get_info(parsed_data):
  '''Returns a list of the relevant info for each professor'''
  info = []
  for i in range(len(d)):
    if i > 0:
      info.append(d[i][1:])
  return info

def professor_dict(parsed_data):
  info = get_info(parsed_data)
  names = get_names(parsed_data)
  fl = []
  for i in names:
    l = i.split(' ')
    fl.append((l[0], l[-1]))
  
  result = dict()
  
  for i in range(len(fl)):
    result[fl[i]] = info[i]
    
  
  
    
  
  

  
