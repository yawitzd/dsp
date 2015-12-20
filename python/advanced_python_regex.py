import os, csv, re


def read_data(file):
  data = open(file)
  d = []
  csv_data = csv.reader(data)
  for row in csv_data:
    d.append(row)
  data.close()
  return d
  
def get_uniqe_degrees(parsed_data):
  '''list of lists --> list of tuples
  
  Takes the parsed data and returns a list of tuples in the format (str, int)
  
  >>> get_unique_degrees(data)
  [('phd', 3), ('jd', 1)]
  '''
  d = parsed_data
  
  raw = []
  for i in range(len(d)):
    if i > 0:
      full.append(d[i][1])
  
  stripped = []
  for item in raw:
    new = re.sub('[.]', '', item.lower())
    stripped.append(new)
  
  degrees = []
  for item in stripped:
    if item != '0':
      personList = re.sub("[^\w]", " ",  item).split()
      for deg in personList:
        degrees.append(deg)
  
  


      
    
  
  
  
  

    
