import entropy
def getGain(data, collection):
  if collection == 'penghasilan':
    limit = 3
    getCollectionKeys = {}
    getCollectionKeys['under_limit'] = {}
    getCollectionKeys['upper_limit'] = {}
    getCollectionKeys['upper_limit']['count'] = 0
    getCollectionKeys['upper_limit']['kredit'] = {}
    getCollectionKeys['upper_limit']['kredit']['layak'] = 0
    getCollectionKeys['upper_limit']['kredit']['tidak_layak'] = 0
    getCollectionKeys['under_limit']['count'] = 0
    getCollectionKeys['under_limit']['kredit'] = {}
    getCollectionKeys['under_limit']['kredit']['layak'] = 0
    getCollectionKeys['under_limit']['kredit']['tidak_layak'] = 0
    for info in data:
      if int(info['penghasilan']) >= limit:
        getCollectionKeys['upper_limit']['count'] += 1
        if info['kredit'] == 'layak':
          getCollectionKeys['upper_limit']['kredit']['layak'] += 1
        else:
          getCollectionKeys['upper_limit']['kredit']['tidak_layak'] += 1
      else:
        getCollectionKeys['under_limit']['count'] += 1
        if info['kredit'] == 'layak':
          getCollectionKeys['under_limit']['kredit']['layak'] += 1
        else:
          getCollectionKeys['under_limit']['kredit']['tidak_layak'] += 1
  else:
    getCollectionKeys = {}
    for info in data:
      if info[collection] in getCollectionKeys.keys():
        getCollectionKeys[info[collection]]['count'] += 1
        if info['kredit'] == 'layak':
          getCollectionKeys[info[collection]]['kredit']['layak'] += 1
        else:
          getCollectionKeys[info[collection]]['kredit']['tidak_layak'] += 1
      else:
        getCollectionKeys[info[collection]] = {}
        getCollectionKeys[info[collection]]['count'] = 1
        getCollectionKeys[info[collection]]['kredit'] = {}
        if info['kredit'] == 'layak':
          getCollectionKeys[info[collection]]['kredit']['layak'] = 1
          getCollectionKeys[info[collection]]['kredit']['tidak_layak'] = 0
        else:
          getCollectionKeys[info[collection]]['kredit']['layak'] = 0
          getCollectionKeys[info[collection]]['kredit']['tidak_layak'] = 1
  gain = entropy.getEntropy(data) - entropy.collection(getCollectionKeys)
  return gain