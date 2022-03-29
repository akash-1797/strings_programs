def replace(str,char1,char2):
  n = len(str)
  new_string = ''
  for i in str:
    if i == char1:
      new_string  = new_string + char2
    else:
      new_string = new_string + i
  return new_string


str = 'abababa'
char1 = 'b'
char2 = 'a'
print(replace(str,char1,char2))
