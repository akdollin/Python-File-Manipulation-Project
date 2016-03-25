"""
acd2164
Akiva Dollin
Homework 2 Part1                                                                                                                                                          
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

  x = None 
  for i,token in enumerate(data[0]):
      if token == "DESCRIPTION":
        x = i
        break
  types = []
  for line in data:
    if line[x]:
       types.append(line[x])
  types.pop(0)
  types = set(types)

  number = len(types)

  return number 

def q2(data):
  """
  @param data the output of load_data()
  @return the number of  distinct `vendor`s (by exact string comparison) in this dataset
  """
  x = None
  for i, token in enumerate(data[0]):
    if token == "VENDOR":
      x = i
      break
  vendor = []
  for line in data:
    if line[x]:
      vendor.append(line[x])
  vendor.pop(0)
  vendor = set(vendor)

  number = len(vendor)
      
  return number 

def q3(data):
  """
  @param data the output of load_data()
  @return the value of the `store` attribute (the id) of the store that had the most sales (as defined by bottle qty)
  """
  x= None
  for i, token in enumerate(data[0]):
    if token == "STORE":
      x = i
      break

  
  j = None
  for j, token1 in enumerate(data[0]):
    if token1 == "BOTTLE QTY":
      y = j
      break

  store = []
  for line in data:
    if line[x]:
      store.append(line[x])
  store.pop(0)
#  print(store[0])
#  exit()
  quantity = []
  for line in data:
    if line[y]:
      quantity.append(line[y])
  quantity.pop(0)    #get rid of the column name
  quantityInt = [int(x) for x in quantity] #convert to ints

  storeQuantity = {}
  storeSet = set(store)
  for eachStore in storeSet:
    storeQuantity[eachStore] = 0

  for store, qty in zip(store, quantityInt):
    storeQuantity[store] +=  qty
  

  import operator
  
  sorted_dict = sorted(storeQuantity.items(), key=operator.itemgetter(1))
  
  
  maxstoreTotal = sorted_dict[-1][0] 
  return maxstoreTotal
  
  # Try using dictionaries for this question, and make use of the sorted function available for list and dictionaries
  # https://docs.python.org/2/tutorial/datastructures.html
def q4(data):
  """
  @param data the output of load_data()
  @return The value of the `description` attribute of the most sold item from the store from q3()
  """
  # Try using dictionaries for this question, and make use of the sorted function available for list and dictionaries
  # https://docs.python.org/2/tutorial/datastructures.html

  maxStore = q3(data)

  x = None
  for i ,token in enumerate(data[0]):
      if token == "STORE":
        x = i
        break

  y = None
  for j, token1 in enumerate(data[0]):
    if token1 == "BOTTLE QTY":
      y = j
      break

  
  z = None 
  for k,token2 in enumerate(data[0]):
      if token2 == "DESCRIPTION":
        z = k 
        break

  mostSold = {}
#  import pdb; pdb.set_trace()
  p = 0 
  for line in data:  
    if p==0:
      p = p + 1
    elif p>0:
      temp = int(line[x])

      if temp == int(maxStore):

        temp2 = int(line[y])
        temp3 = line[z]
        mostSold[temp2] = temp3

  maxQuan = max(mostSold)
  

  result = mostSold[maxQuan]
  return result

def q5(data):
  """
  Finds the `zipcode` that has the greatest total `bottle_qty` for `category_name` "TEQUILA"
  @param data the output of load_data()
  @return The value of the `zipcode` attribute with the most sales in "TEQUILA" category
  """
  # Try using dictionaries for this question, and make use of the sorted function available for list and dictionaries
  # https://docs.python.org/2/tutorial/datastructures.html
  x = None
  for i ,token in enumerate(data[0]):
      if token == "CATEGORY NAME":
        x = i
        break

  y = None
  for j, token1 in enumerate(data[0]):
    if token1 == "BOTTLE QTY":
      y = j
      break


  z = None
  for k,token2 in enumerate(data[0]):
      if token2 == "ZIPCODE":
        z = k
        break

  category = []
  for line in data:
    if line[x]:
      category.append(line[x])
  category.pop(0)

      
  zipCode = []
  for line in data:
    if line[z]:
      zipCode.append(line[z])
  zipCode.pop(0)


  quantity = []
  for line in data:
    if line[y]:
      quantity.append(line[y])
  quantity.pop(0)    #get rid of the column name
  quantityInt = [int(x) for x in quantity] #convert to ints

  zipQuantity = {}
  zipSet = set(zipCode)
  for eachZip in zipSet:
    zipQuantity[eachZip] = 0 

  for zip_code, cat, qty in zip(zipCode, category,  quantityInt):
    if cat == "TEQUILA":
      zipQuantity[zip_code] += qty

    
    
    #print(qty)

  import operator
  
  sorted_dict = sorted(zipQuantity.items(), key=operator.itemgetter(1))
  
  
  maxZipTotal = sorted_dict[-1][0]

  return maxZipTotal

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
