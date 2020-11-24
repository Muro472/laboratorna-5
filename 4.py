n = int(input('ведіть n'))
x0 = 0
x1 = 9
x2 = 9
i = 1
if n == 1:
    s = x1
elif n == 2:
    s = x1
else:
    while i < n:
        i += 1
        x3 = x2 + x0 * 4
        x0 = x2
        x2 = x3
    s = x3
print("x{0} = {1}".format(n,s))