def counting_in_string(str):
  vowels = 0
  cons_s = 0
  numbers = 0
  special_char = 0
  
  for char in str:
    if (char >= 'a' and char <='z') or (char >='A' and char <='Z'):
      char = char.lower()
      if char =='a' or char == 'e' or char == 'i' or char =='o' or char == 'u':
        vowels = vowels+1
      else:
        cons_s = cons_s +1
    elif char >= '0' and char <='9':
      numbers = numbers+1
    else:
      special_char = special_char +1
  return vowels,cons_s,numbers,special_char

str = 'aiouNSVDLGmgerng123m456+?gm !#embr MMK'
print(counting_in_string(str))
