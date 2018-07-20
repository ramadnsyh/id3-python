import json
import gain
with open('data.json') as json_data:
  data = json.load(json_data)

gainArr = []
for key in data[0].keys():
  if key != 'name' and key != 'kredit':
    obj = {}
    obj['title'] = key
    obj['gain'] = gain.getGain(data, key)
    gainArr.append(obj)

print(gainArr)
def findMaxValue(arr):
  value = arr[0]
  for i in range(1, len(arr)):
    if value['gain'] < arr[i]['gain']:
      value = arr[i]
  return value
print(findMaxValue(gainArr))
