def palindrome(str):
  n = len(str)
  flag = 0
  l = 0
  m = (n-1)//2
  r = n-1
  while(l <= m ):
    if str[l] == str[r]:
      l = l+1
      r = r-1
    else:
      flag = 1
      break
  if flag == 1:
    return False
  else:
    return True

print(palindrome('racecar'))

