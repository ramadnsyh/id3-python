def getPrediction(data, target, title):
  temp = {}
  for info in data:
    if info[title] in temp.keys():
      if info['kredit'] == 'layak':
        temp[info[title]]['layak'] += 1
      else:
        temp[info[title]]['tidak_layak'] += 1
    else:
      temp[info[title]] = {}
      if info['kredit'] == 'layak':
        temp[info[title]]['layak'] = 1
        temp[info[title]]['tidak_layak'] = 0
      else:
        temp[info[title]]['layak'] = 0
        temp[info[title]]['tidak_layak'] = 1
  print(target, title)
  if title == 'penghasilan':
    for key in temp:
      limit = 3
      count_data = 0
      for status in temp[key]:
        count_data += int(temp[key][status])
      if int(key) >= limit:
        for info in temp[key]:
          print(temp)
          if temp[key][info] == count_data:
            return info
          else:
            isPredict = False
      else:
        for info in temp[key]:
          if temp[key][info] == count_data:
            return info
          else:
            isPredict = False
  else:
   for key in temp:
     count_data = 0
     for status in temp[key]:
       count_data += int(temp[key][status])
     for info in temp[key]:
       print(title)
       if temp[key][info] == count_data:
         return info
       else:
         isPredict = False
  
  return isPredict