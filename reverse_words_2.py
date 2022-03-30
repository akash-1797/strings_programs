def fun(str):
  n = len(str)
  res = ''
  i = 0
  while(i<n):
    while(i<n and str[i]==' '):
      i = i+1
    if (i >= n):
      break 
    j = i+1
    while(j<n and str[j] != ' '):
      j = j+1
    word = str[i:j]
    if len(res) == 0:
      res = word
    else:
      res = word + ' ' + res
    i = j +1
  return res 

str = '   my     favourite  game is  football   '
print(fun(str))
  
