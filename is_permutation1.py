def is_permutation(str1,str2):
  n1 = len(str1)
  n2 = len(str2)
  if n1 != n2:
    return False 
    
  a = sorted(str1)
  str1 = ' '.join(a)
  b = sorted(str2)
  str2 = ' '.join(b)
  print(str1)
  print(str2)

  i = 0
  j = 0
  while(i<=n1-1 and j <=n2-1):
    if str1[i] != str2[j]:
      return False
    i = i+1
    j = j+1
  return True
  

str1 = 'listen'
str2 = 'silent'
print(is_permutation(str1,str2))
