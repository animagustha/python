# Sum of numbers in a list


def listsum(a):
    add = 0
    for key in a:
        add += key
    return add

li = [1, 2, 3, 4, 5]
print(listsum(li))
