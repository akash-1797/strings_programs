def palindrome(str):
  n = len(str)
  left = 0
  right = n-1
  while(left < right):
    if str[left] != str[right]:
      return False
    left = left +1
    right = right - 1
  return True

str = 'madam'
print(palindrome(str))
