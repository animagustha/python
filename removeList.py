li = [58, 100, 2, 85, 68, 900]
size = len(li)
for key in reversed(li):
    if key%2 == 0:
        li.remove(key)
print(li)
