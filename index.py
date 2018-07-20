import json
import gain
import predict
with open('data.json') as json_data:
  data = json.load(json_data)

def findMaxValue(arr):
  value = arr[0]
  for i in range(1, len(arr)):
    if value['gain'] < arr[i]['gain']:
      value = arr[i]
  return value

def decision(data, target):
  gainArr = []
  for key in data[0].keys():
    if key != 'name' and key != 'kredit':
      obj = {}
      obj['title'] = key
      obj['gain'] = gain.getGain(data, key)
      gainArr.append(obj)
  
  maxValue = findMaxValue(gainArr)
  prediction = predict.getPrediction(data, target, maxValue['title'])
  if prediction == False:
    newData = []
    for i in range(len(data)): 
      if data[i][maxValue['title']] == target[maxValue['title']]:
        newData.append(data[i])
    return decision(newData, target)
  return prediction

target = {
    "penghasilan": ">3x angsuran",
    "pekerjaan": "honorer",
    "sikap": "berkelakuan baik",
    "kepemilikan": "kontrak",
}
print(decision(data, target))