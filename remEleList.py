def rem(a, b):
    # count = 0
    for key in reversed(remove):
        a.remove(a[key])
        # count += 1
    return a

li = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
remove = [0, 4, 5]
print(rem(li, remove))
