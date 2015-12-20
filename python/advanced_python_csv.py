import os, csv, re


def read_data(file):
  data = open(file)
  d = []
  csv_data = csv.reader(data)
  for row in csv_data:
    d.append(row)
  data.close()
  return d
  
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

emails = get_emails(read_data('faculty.csv'))

with open('emails.csv', 'w') as f:
	a = csv.writer(f)
	for item in emails:
		a.writerow([item])
	f.close()

