def highestOccuringChar(string) :
  n = len(string)
  no_of_char = 256
  count = [0]*no_of_char
  for i in string:
    count[ord(i)] += 1
    max = count[ord(string[0])]
    ans = string[0]
  for i in range(1,n):
    if count[ord(string[i])] > max:
      max = count[ord(string[i])]
      ans = string[i]
  return ans

string ='aabbaabalhdhebbbbd'
print(highestOccuringChar(string))
