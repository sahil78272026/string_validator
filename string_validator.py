if __name__ == '__main__':
    s = input()
    
    for ch in s:
        bool = False
        if ch.isalpha() or ch.isdigit():
            bool = True
            break

    print(bool)
    

    for ch in s:
        bool = False
        if ch.isalpha():
            bool = True
            break

    print(bool)

    for ch in s:
        bool = False
        if ch.isdigit():
            bool = True
            break

    print(bool)

    for ch in s:
        bool = False
        if ch.islower():
            bool = True
            break

    print(bool)

    for ch in s:
        bool = False
        if ch.isupper():
            bool = True
            break

    print(bool)
    