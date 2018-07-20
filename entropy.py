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
  total_entropy = 0
  for status in result:
    if result[status] == 0:
      return total_entropy
  for count in result.keys():
    total_entropy += ( (-result[count] / total) * ( log(result[count] / total, 2)))
  return total_entropy

def collection(data):
  total_entropy = 0
  total_data = 0
  total_key = 0
  ## CHECK ENTROPY
  for key in data:
    for status in data[key]['kredit']:
      if data[key]['kredit'][status] == 0:
        return total_entropy
  
  ## GET TOTAL COUNT
  for key in data:
    total_data += data[key]['count']
  for key in data:
    total_key = data[key]['count']
    for info in data[key]['kredit']:
      total_entropy += (( -1 * data[key]['kredit'][info] / total_key ) * (log(data[key]['kredit'][info] / total_key, 2)))
    total_entropy *= total_key / total_data
  return total_entropy