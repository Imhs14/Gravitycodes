"""
Task
The provided code stub reads two integers, a and b, from STDIN.

Add logic to print two lines. The first line should contain the result of integer division, a //b . The second line should contain the result of float division, a/b .

No rounding or formatting is necessary.
4
3
Sample Output 0

1
1.33333333333
"""
a = int(input(""))
b = int(input(""))
c = a//b
d = a/b
print(c)
print(f"{d:.2f}")