def pattern(n):
    for key in range(1, n+1):
        for i in range(1, key+1):
            print(key, end=' ')
        print()

pattern(9)
