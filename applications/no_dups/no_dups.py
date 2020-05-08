def no_dups(s):
    cache = {}
    new_s = ''
    for w in s.split():
        if w not in cache:
            new_s = new_s + ' ' + w
            cache[w] = 1
    return new_s.strip()


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
