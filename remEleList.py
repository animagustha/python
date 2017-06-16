def rem(a, b):
    count = 0
    for key in b:
        a.remove(a[key-count])
        count += 1
    return a

li = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
remove = [0, 4, 5]
print(rem(li, remove))
