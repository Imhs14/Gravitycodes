import string

def print_rangoli(size):
    letters = string.ascii_lowercase[:size]
    
    rows = []
    for i in range(size):
        part = letters[size-1-i : size]
        row_str = '-'.join(part[::-1]) + ('-' + '-'.join(part[1:]) if part[1:] else '')
        rows.append(row_str)
    
    width = len(rows[-1])  # middle row is always the longest
    rows = [r.center(width, '-') for r in rows]
    
    full = rows + rows[-2::-1]
    print('\n'.join(full))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


'''
Here is the main logic for your reference 

for i in range(size):        # i is the row number: 0, 1, 2, 3, 4
    part = letters[size-1-i : size]
    # row 0 → letters[4:5] → 'e'
    # row 1 → letters[3:5] → 'de'
    # row 2 → letters[2:5] → 'cde'
    # row 3 → letters[1:5] → 'bcde'
    # row 4 → letters[0:5] → 'abcde'

'-'.join(part[::-1])   # 'e-d-c'
'-'.join(part[1:])     # 'd-e'

row_str = '-'.join(part[::-1]) + '-' + '-'.join(part[1:])
# → 'e-d-c' + '-' + 'd-e'
# → 'e-d-c-d-e'  

That's the complete logic. part[1:] skips c because it's already the center, and you don't want e-d-c-c-d-e.

('-' + '-'.join(part[1:]) if part[1:] else '')
Only adds the - and right side if part[1:] is not empty. For size=1, part = 'a', so part[1:] is empty → just prints a. ✅
'''