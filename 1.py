n = float(input('Введіть число n:'))
i=1
first_dodanok = 0
seckond_dodanok = 0
while i <= n:
    first_dodanok = first_dodanok + (2 * i)**2
    i += 1
else:
    i = 1
    while i <= n:
        seckond_dodanok = seckond_dodanok + (2 * i + 1) ** 3
        i += 1
    else:
        print('значення виразу:', first_dodanok + seckond_dodanok)
