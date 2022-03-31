def remove_consecutive_char(string):
  new = ''
  pre = ''
  for char in string:
    if len(new)==0:
      new = new +char
      pre  = char
    if char == pre:
      continue
    else:
      new = new +char
      pre  = char
  return new 
string = 'aabbccddd'
print(remove_consecutive_char(string))
