# To check if a list is empty


# implementation 1
def list_empty(a):
    if not a:
        print('empty list')
    else:
        print('non empty list')


list_empty([])
list_empty([1, 2, 3])

# implementation 2


def is_empty(a):
    if len(a) is 0:
        return "empty"
    else:
        return "List is not empty"


print(is_empty([]))
print(is_empty([1, 2, 3]))
