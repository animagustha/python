"""
Write a program that count number of characters in a string and
display,s the count of each word along with the word
"""


# using only lists


def dups(a):
    b = []
    c = []
    j = 0
    for key in a:
        if key not in b:
            b.append(key)
            c.append(a.count(key))
    for key in b:
        print(key, c[j])
        j += 1

s = 'google'
print(dups(s))


# using Dictionaries


def dup_num(a):
    d = {}
    for character in a:
        if character not in d:
            d[character] = 1
        else:
            d[character] += 1
    return d

print(dup_num(s))
