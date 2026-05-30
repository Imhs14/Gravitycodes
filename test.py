import string

size = 5
letters = string.ascii_letters[:size]

x = '-'.join(letters[1:])
y = '-'.join(letters[::-1])
z = y + '-' + x # mid line

p = letters[size-1:].center((2*size-1)*2-1,'-')
print(p)
c = '-'.join(letters[size-2:])
print(c.center((2*size-1)*2-1,'-'))
v = '-'.join(letters[size-3:])
print(v.center(len(z),'-'))

print(z)

while 
