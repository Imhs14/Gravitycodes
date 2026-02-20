"""
TASK:
the provided code stub reads an integer, n, from STDIN.
for all non-negative integers i<n, print i^2.
"""
n = int(input(""))
i = 0
while i<n:
    print(i*i)
    i += 1

"""
example input: 4 # i.e 0,1,2,3
example output:
0
1
4
9
"""