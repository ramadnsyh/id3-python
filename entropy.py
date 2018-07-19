from math import log
def getEntropy(data):
  result = {} 
  for i in range(len(data)):
    if data[i]['kredit'] in result.keys():
      result[data[i]['kredit']] += 1
    else:
      result[data[i]['kredit']] = 1
  
  total = 0
  for count in result.keys():
    total += result[count]
  total_entryopy = 0
  for count in result.keys():
    total_entryopy += ( (-result[count] / total) * ( log(result[count] / total, 2)))
  return total_entryopy