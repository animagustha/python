"""
Write a Python program to remove duplicates from a list.
"""


def dup_removal(a):
    new_list = []
    for key in a:
        if key not in new_list:
            new_list.append(key)
    return new_list

li = ['Debian', 'Ubuntu', 'Arch', 'Gentoo', 'Fedora', 'CentOS', 'OpenSUSE', 'Arch', 'Gentoo']
print(dup_removal(li))
