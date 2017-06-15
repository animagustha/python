# To find a largest number in a list


def large(a):
    temp = 0
    for key in a:
        if key > temp:
            temp = key

    return temp

li = [58, 100, 2, 85, 68, 900]
print(large(li))
