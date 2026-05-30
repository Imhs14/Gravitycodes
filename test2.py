import string

size = 3
letters = string.ascii_letters[i:size]

x = '-'.join(letters[1:])
y = '-'.join(letters[::-1])
z = y + '-' + x # mid line

ln1 = (letters[size-1:]).center(len(z),'-')
print(ln1) # line 1 sorted 

ln2 = ((letters[size-1:]) + '-' +(letters[size-2:size-1]) + '-' + (letters[size-1:])).center(len(z),'-')
print(ln2) # line 2

print(z) # line mid sorted


ln3 = ((letters[size-1:]) + '-' +(letters[size-2:size-1]) + '-' + (letters[size-1:])).center(len(z),'-')
print(ln3) # line 3

ln4 = (letters[size-1:]).center(len(z),'-')
print(ln4) # line 4
