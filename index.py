import json
import entropy
with open('data.json') as json_data:
  data = json.load(json_data)

print(entropy.getEntropy(data))

