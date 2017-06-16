def copy(a):
    b = a       # shallow copy
    print(b)
    a[2] = 5
    print(a, b)

    c = a[:]    # deep copy
    a.append(6)
    print(a, c)

    d = list(a)
    print(d)
    a.pop()
    print(a, d)
    a.append(10)
    print(a, d)

copy([1, 2, 3])
