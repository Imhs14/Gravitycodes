if __name__ == '__main__':
    n = int(input())
    # Read the whole line, split into strings, and convert each to an int
    integer_list = map(int, input().split())
    
    # Create the tuple
    t = tuple(integer_list)
    
    # Print the hash
    print(hash(t)) 
    # worker with python 2

"""
example 
i/p :
2
1 2
o/p :
3713081631934410656
"""