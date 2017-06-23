def multi_table(n):
    for i in range(1, 11):
        print(n, ' * ', i, ' = ', int(n)*i )

while True:
    try:
        a = input('enter the number')
        multi_table(a)
        break
    except ValueError:
        print('please enter an integer value')

