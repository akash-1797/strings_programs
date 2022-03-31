def fun(str1,str2):
  no_of_char  = 256
  n1 = len(str1)
  n2 = len(str2)
  if n1 != n2:
    return False
  count1 = [0]*no_of_char
  count2 = [0]*no_of_char

  for i in str1:
    count1[ord(i)] += 1
  for i in str2:
    count2[ord(i)] += 1

  for i in range(no_of_char):
    if count1[i] != count2[i]:
      return False
  return True

str1 = 'akash'
str2 = 'akahh'
print(fun(str1,str2))

