string = input('n=')
x = 0
temp = ''
for i in string:
    if i not in temp:
        temp = temp + i
        x=string.count(i)
        print(f'{i} {x}')
