n1 = int(input('Введіть число n:'))
i = 1
k = 1
n2 = 0
length = -2
while i != 0:
    i = n1 // k
    k = k * 10#знаходження довжини числа
    length += 1
a = 10 ** length
i = 1
p = 1
while i != 0:
    i = n1 // a
    n1 = n1 - (a * i)
    a = a / 10
    n2 = (i * p) + n2
    p = p * 10
print(n2)
