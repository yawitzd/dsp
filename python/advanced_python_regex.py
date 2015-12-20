import os, csv, re


def read_data(file):
  data = open(file)
  d = []
  csv_data = csv.reader(data)
  for row in csv_data:
    d.append(row)
  data.close()
  return d
  
def get_unique_degrees(parsed_data):
  '''list of lists --> dict
  
  Takes the parsed data and returns a dict of format str,int
  
  >>> get_unique_degrees(data)
  {'phd':1, 'jd':2}
  '''
  d = parsed_data
  
  raw = []
  for i in range(len(d)):
    if i > 0:
      raw.append(d[i][1])
  
  stripped = [] #remove periods and make lowercase
  for item in raw:
    new = re.sub('[.]', '', item.lower())
    stripped.append(new)
  
  degrees = [] #take each person's degrees and add them to the total
  for item in stripped:
    if item != '0':
      personList = re.sub("[^\w]", " ",  item).split()
      for deg in personList:
        degrees.append(deg)
  
  uniques = dict()
  for item in degrees:
    if item not in uniques:
      uniques[item] = 1
    else:
      uniques[item] += 1
  return uniques
  
  
def get_unique_titles(parsed_data):
  '''list of lists -> dict
  
  Take the parsed data and returns a dict of titles and their counts. 
  
  >>> get_unique_titles(data)
  {'assistant professor':1, 'adjunt':2}
  '''
  d = parsed_data
  
  raw = []
  for i in range(len(d)):
    if i > 0:
      raw.append(d[i][2])
      
  uniques = dict()
  for item in raw:
    if item not in uniques:
      uniques[item] = 1
    else:
      uniques[item] += 1
  return uniques
  
def get_emails(parsed_data):
  '''list of lists -> list
  
  Take the parsed data and returns a list of emails. 
  
  >>> get_emails(data)
  ['ben@yahoo.com', 'paul@hotmail.com']
  '''
  d = parsed_data
  
  raw = []
  for i in range(len(d)):
    if i > 0:
      raw.append(d[i][3])
  return raw
  

def get_unique_domains(parsed_data):
  '''list of lists -> list
  
  Take the parsed data and returns a list of domains. 
  
  >>> get_unique_domains(data)
  ['yahoo.com', 'hotmail.com']
  '''
  e = get_emails(parsed_data)
  dom = []
  for item in e:
    dom.append(item.split('@')[1])
  
  uniques = []
  for item in dom:
    if item not in uniques:
      uniques.append(item)
      
  return uniques
  
    
  
  
  


      
    
  
  
  
  

    
