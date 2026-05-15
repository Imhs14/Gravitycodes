if __name__ == '__main__':
    s = input()
    i = 0
    while len(s[i])<1000 and len(s[i])>0:
        print(any(char.isalnum() for char in s))
        print(any(char.isalpha() for char in s))
        print(any(char.isdigit() for char in s))
        print(any(char.islower() for char in s))
        print(any(char.isupper() for char in s))
        break
"""
example i/p , o/p :
qA2
True
True
True
True
True
"""         
"""
string.isalnum() - (a-z), (A-Z), (0-9)
str.isalpha() - (a-z), (A-Z)
str.isdigit() - (0-9)
str.islower() - (a-z)
str.isupper() - (A-Z)
"""
