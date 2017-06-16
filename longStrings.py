def long_strings(a, n):
    for key in a:
        if len(key) > n:
            print(key, end=' ')
    print()

long_strings(['hello', 'liril', 'text', 'I', 'me', 'U'], 3)
long_strings(['hello', 'liril', 'text', 'I', 'me', 'U'], 1)
