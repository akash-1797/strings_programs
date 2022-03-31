def fun2(str1,str2):
  no_of_char = 256 
  n1 = len(str1)
  n2 = len(str2)
  if n1 != n2 :
    return  False
  count = [0]*no_of_char 
  i = 0
  
  while(i<=n1-1 and i<=n2-1):
    count[ord(str1[i])] += 1
    count[ord(str2[i])] -=1
    i = i+1

  for i in range(no_of_char):
    if count[i]:
      return False
  return True

str1 = 'race'
str2 = 'rate'
print(fun2(str1,str2))

