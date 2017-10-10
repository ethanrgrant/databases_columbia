"""
Columbia W4111 Intro to databases
Homework 2
"""

import sys
from collections import *

def load_data(file_path):
  """
  This method reads the dataset, and returns a list of rows.
  Each row is a list containing the values in each column.
  """
  import csv
  with file(file_path) as f:
    dialect = csv.Sniffer().sniff(f.read(2048))
    f.seek(0)
    reader = csv.reader(f, dialect)
    return [l for l in reader]


def q1(data):
  """
  @param data the output of load_data()
  @return the number of  distinct types of items (by `description` attribute) in this dataset
  """
  
  index = 0
  for types in data[0]:
	if types=="DESCRIPTION":
		break
	index += 1
	
  types = set()
  for line in data[1:]:
	types.add(line[index])

		
  # Try using set for this question (https://docs.python.org/2/tutorial/datastructures.html)
  return len(types)

def q2(data):
  """
  @param data the output of load_data()
  @return the number of  distinct `vendor`s (by exact string comparison) in this dataset
  """
  index = 0
  for types in data[0]:
	if types=="VENDOR":
		break
	index += 1

	
  types = []
  for line in data[1:]:
	types.append(line[index])
	
  types = set(types)
  
  # Try using set for this question (https://docs.python.org/2/tutorial/datastructures.html)
  return len(types)

def q3(data):
  """
  @param data the output of load_data()
  @return the value of the `store` attribute (the id) of the store that had the most sales (as defined by bottle qty)
  """
  qty_index = 0
  for types in data[0]:
	if types=="BOTTLE QTY":
		break
	qty_index += 1

  ven_index = 0
  for types in data[0]:
	if types=="STORE":
		break
	ven_index += 1
	
  sales = dict()

  for line in data[1:]:
	if line[ven_index] in sales:
		update = int(sales[line[ven_index]])+int(line[qty_index])
		sales[line[ven_index]] = update
	else:
		sales[line[ven_index]] = int(line[qty_index])
	

  # Try using dictionaries for this question, and make use of the sorted function available for list and dictionaries
  # https://docs.python.org/2/tutorial/datastructures.html
  
  return max(sales, key=sales.get)

def q4(data):
  """
  @param data the output of load_data()
  @return The value of the `description` attribute of the most sold item from the store from q3()
  """
  qty_index = 0
  for types in data[0]:
	if types=="BOTTLE QTY":
		break
	qty_index += 1

  ven_index = 0
  for types in data[0]:
	if types=="STORE":
		break
	ven_index += 1
 
  sales = dict()
  first = True
  for line in data:
	if not first:
		if line[ven_index] in sales:
			update = int(sales[line[ven_index]])+int(line[qty_index])
			sales[line[ven_index]] = update
		else:
			sales[line[ven_index]] = int(line[qty_index])
	else:
		first = False
  top_store = max(sales, key=sales.get)
  
  des_index = 0
  for types in data[0]:
	if types=="DESCRIPTION":
		break
	des_index += 1
	
  des_bot = dict()
  for line in data[1:]:
	if line[ven_index]==top_store:
		if line[des_index] in des_bot:
			update = int(des_bot[line[des_index]])+int(line[qty_index])
			des_bot[line[des_index]] = update
		else:
			des_bot[line[des_index]] = int(line[qty_index])

  # Try using dictionaries for this question, and make use of the sorted function available for list and dictionaries
  # https://docs.python.org/2/tutorial/datastructures.html
  for store in des_bot:
	print store + " " + str(des_bot[store])
  return max(des_bot, key=des_bot.get)

def q5(data):
  """
  Finds the `zipcode` that has the greatest total `bottle_qty` for `category_name` "TEQUILA"
  @param data the output of load_data()
  @return The value of the `zipcode` attribute with the most sales in "TEQUILA" category
  """
  # Try using dictionaries for this question, and make use of the sorted function available for list and dictionaries
  # https://docs.python.org/2/tutorial/datastructures.html
  qty_index = 0
  for types in data[0]:
	if types=="BOTTLE QTY":
		break
	qty_index += 1
	
  cat_index = 0
  for types in data[0]:
	if types=="CATEGORY NAME":
		break
	cat_index += 1
  
  zip_index = 0
  for types in data[0]:
	if types=="ZIPCODE":
		break
	zip_index += 1
  
  zip_teq= dict()
  for line in data[1:]:
	
	if line[cat_index]=="TEQUILA":
		if line[zip_index] in zip_teq:
			update = int(zip_teq[line[zip_index]])+int(line[qty_index])
			zip_teq[line[zip_index]] = update
		else:
			zip_teq[line[zip_index]] = int(line[qty_index])
  
  
  return max(zip_teq, key=zip_teq.get)

if __name__ == '__main__':
  if len(sys.argv) != 2:
    sys.stderr.write("Usage: python hw2.py (path to input csv)\n")
    sys.exit(1)
  file_path = sys.argv[1]

  data = load_data(file_path)
  print q1(data)
  print q2(data)
  print q3(data)
  print q4(data)
  print q5(data)
