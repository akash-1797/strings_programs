def remove(str,position):
  res = ''
  for i in range(len(str)):
    if i != (position-1):
      res = res + str[i]
  return res

str = 'asdfgghff'
position = 3
print(remove(str,position))
