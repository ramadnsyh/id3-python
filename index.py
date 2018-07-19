import json
import entropy
import gain
with open('data.json') as json_data:
  data = json.load(json_data)

base_entropy = entropy.getEntropy(data)
print(base_entropy)

for key in data[0].keys():
  if key != 'name' and key != 'kredit':
    print(gain.getGain(data, key))