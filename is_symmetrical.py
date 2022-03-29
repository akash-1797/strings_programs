def is_symmetrical(str):
  flag = 0
  n = len(str)
  if n % 2 == 0:
    mid = n//2
  else:
    mid = (n+1)//2
  start_1 = 0
  start_2 = mid
  while(start_1 < mid and start_2 < n):
    if str[start_1] == str[start_2]:
      start_1 = start_1 + 1
      start_2 = start_2 + 1
    else:
      flag = 1
      break
  if flag == 1:
    return False
  else:
    return True


str = "babababa"
print(is_symmetrical(str))

