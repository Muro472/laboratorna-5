n = input('Введіть число n:')
b = list(n)
len = len(n)
i = 0
list1 = ''
while len > i:
    list1 = str(b[i]) + list1
    i += 1
print(list1)