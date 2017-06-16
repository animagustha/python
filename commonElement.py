temp = ['hello', 'liril', 'text', 'I', 'me', 'U']
temp1 = ['never', 'world', 'text', 'I', 'google', 'U']
li = [1, 2, 3, 4, 5]
li1 = [6, 7, 8, 9, 5]


def common_element(temp, temp1):
    for key in temp1:
        if key in temp:
            return True
    return False

print(common_element(temp, temp1))
print(common_element(temp, li))
print(common_element(li, li1))