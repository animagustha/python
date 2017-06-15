"""
Write a Python program to count the number of strings where the
string length is 2 or more and the first and last character
are same from a given list of strings.
"""


# Implementation 1


def str_len_method1(a):
    # print('from method one')
    count = 0
    for key in a:
        if len(key) < 2:
            continue
        if key[0] is key[len(key) - 1]:
            count += 1
    return count


li = ['hello', 'text', 'I', 'me', 'U', 'tempt', 'liril']
print(str_len_method1(li))


# Implementation 2


def str_len(a):
    # print('from method two')
    count = 0
    for key in a:
        if len(key) < 2:
            continue
        if char_check(key):
            count += 1
    return count


def char_check(key):

    if key[0] is key[len(key)-1]:
        return True

li = ['hello', 'liril', 'text', 'I', 'me', 'U']

print(str_len(li))


# Implementation 3


def str_len_method3(a):
    # print('from method one')
    count = 0
    for key in a:
        if len(key) >= 2:
            if key[0] is key[len(key) - 1]:
                count += 1
    return count


li = ['hello', 'text', 'I', 'me', 'U', 'tempt', 'liril', 'level']
print(str_len_method3(li))
