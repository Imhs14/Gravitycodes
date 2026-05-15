def split_and_join(line):
    line.split(" ")
    c="-".join(line)
    return c
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

"""
Eg : i/p & o/p - 
Helloooooo
H-e-l-l-o-o-o-o-o-o
"""