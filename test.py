s = input('')
b = s.split()
lst = []
for i in range(len(b)):
    lst.append(b[i].capitalize())

print(' '.join(lst))