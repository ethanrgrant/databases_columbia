from collections import *
import pdb

def load_data(file_path):

  import csv
  with file(file_path) as f:
    dialect = csv.Sniffer().sniff(f.read(2048))
    f.seek(0)
    reader = csv.reader(f, dialect)
    return [l for l in reader]

def q1(data):

  # Try using set for this question (https://docs.python.org/2/tutorial/datastructures.html)

  ret = set()
  for row in data:
    ret.add(row[15])
  return len(ret) - 1

def q2(data):

  # Try using set for this question (https://docs.python.org/2/tutorial/datastructures.html)

  ret = set()
  for row in data:
    ret.add(row[13])
  return len(ret) - 1

def q3(data):

  # Try using dictionaries for this question, and make use of the sorted function available for list and dictionaries
  # https://docs.python.org/2/tutorial/datastructures.html

  d = defaultdict(lambda: 0)
  for row in data[1:]:
    d[row[2]] += int(row[20])

  return sorted(d.items(), key=lambda p: p[1])[-1][0]

def q4(data):

  # Try using dictionaries for this question, and make use of the sorted function available for list and dictionaries
  # https://docs.python.org/2/tutorial/datastructures.html

  storeid = q3(data)
  d = defaultdict(lambda: 0)

  for row in data[1:]:
    if row[2] == storeid:
      d[row[15]] += int(row[20])
  for stuff in d:
	print stuff + " " + str(d[stuff])
  return sorted(d.items(), key=lambda p: p[1])[-1][0]

def q5(data):
 
  # Try using dictionaries for this question, and make use of the sorted function available for list and dictionaries
  # https://docs.python.org/2/tutorial/datastructures.html

  category = "TEQUILA"
  d = defaultdict(lambda: 0)

  for row in data[1:]:
    if row[11] == category:
      d[row[6]] += int(row[20])

  return sorted(d.items(), key=lambda p: p[1])[-1][0]

if __name__ == '__main__':
  file_path= "liq.csv"
  def run(file_path):
    data = load_data(file_path)
    print q1(data)
    print q2(data)
    print q3(data)
    print q4(data)
    print q5(data)

  run(file_path)