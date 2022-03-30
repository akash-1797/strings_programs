def count_vowel(str):
  count = 0
  b = [] 
  v = ['a','e','i','o','u']
  for i in str :
    if i in v and i not in b:
      b.append(i)
      count = count+1
  print(b)
  return count

str = 'aivcomeuaoe'
print(count_vowel(str))
      
