def karatsuba(x, y):
    x, y = _balance((x, y))
    n = len(str(x))

    if n > 1:
        a = str(x)[0:int(n/2)]
        b = str(x)[int(n/2):]
        c = str(y)[0:int(n/2)]
        d = str(y)[int(n/2):]
        a, b, c, d = int(a), int(b), int(c), int(d)

        if len(str(a)) > 1:
            ac = karatsuba(a, c)
            bd = karatsuba(b, d)
            abcd = karatsuba(a + b, c + d)
        else:
            ac = a*c
            bd = b*d
            abcd = (a+b)*(c+d)

        return 10 ** n * ac + 10 ** int(n / 2) * (abcd - ac - bd) + bd
    else:
        return int(x) * int(y)


def _balance(val):
    x = str(val[0])
    y = str(val[1])

    while len(x) % 2 != 0:
        x = '0' + x
    while len(y) % 2 != 0:
        y = '0' + y

    while len(x) > len(y):
        y = '0' + y
    while len(y) > len(x):
        x = '0' + x

    return x, y

print(karatsuba(1685287499328328297814655639278583667919355849391453456921116729,
                7114192848577754587969744626558571536728983167954552999895348492))
