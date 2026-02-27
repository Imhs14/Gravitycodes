def swap_case(s):
    if 0<len(s) and len(s)<=1000:
        res = s.swapcase()
    return res

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

"""
example i/p & O/P:

HEEraShAnker234MALathkar
heeRAsHaNKER234malATHKAR
"""


# An alternate method of solving the same question
"""
if __name__ == '__main__':
    s = input()
    result = s.swapcase()
    print(result)
    """