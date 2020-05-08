
import re

def word_count(s):
    cache = {}
    s = s.translate({ord(c): " " for c in "\": ; , . - + = / \ | [ ] { } ( ) * ^ &"})
    for w in s.split():
        w = w.lower()
        if w not in cache:
            cache[w] = 1
        else:
            cache[w] += 1
    return cache



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
