string = 'india will win football world cup one day'
x = string.split(' ')
print(x)
n = len(x)
i = 0
while(i<n//2):
  x[i],x[n-i-1] = x[n-i-1],x[i]
  i = i+1
y = ' '.join(x)
print(y)
