def tot(li):
    res = 0
    for key in li:
        res += key
    print('sum = ', res)
    return res


def avg(result, n):
    average = result // n
    print('average is ', average)


a = []
boolean = True
while boolean:
    while True:
        try:
            temp = int(input('enter the number'))
            break
        except ValueError:
            print('enter integer value')

    if temp is not 0:
        a.append(temp)
    else:
        break
# tot()
avg(tot(a), len(a))