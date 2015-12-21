import os, csv, re
os.chdir('Metis/prework')

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

def faculty_dict(parsed_data):
  d = parsed_data
  names = get_names(parsed_data)
  info = get_info(parsed_data)
  
  
  lasts = []
  for i in names:
    l = i.split(' ')
    lasts.append(l[-1])
  
  fac_dict = dict()
  for i in range(len(lasts)):
    name = lasts[i]
    inf = info[i]
    if name in fac_dict:
      fac_dict[name].append(inf)
    else:
      fac_dict[name] = [inf]

#Q7
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
  
  return result

#Q8
def professor_dict_rev(parsed_data):
  info = get_info(parsed_data)
  names = get_names(parsed_data)
  lf = []
  for i in names:
    l = i.split(' ')
    lf.append((l[-1], l[0]))
  
  result = dict()
  
  for i in range(len(lf)):
    result[lf[i]] = info[i]    
  return result
  
    
  
  

  
