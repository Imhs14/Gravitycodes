"""
insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
"""
if __name__ == '__main__':
    N = int(input())
    mylist = []
    for _ in range(N):
        command , *args = input().split()
        if command == 'insert':
            mylist.insert(int(args[0]), int(args[1]))
        elif command == 'remove':
            mylist.remove(int(args[0]))
        elif command == 'append':
            mylist.apped(int(args[0]))
        elif command == 'sort':
            mylist.sort()
        elif command == 'pop':
            mylist.pop()
        elif command == 'reverse':
            mylist.reverse()
        elif command == 'print':
            print(mylist)

"""
example i/p:
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

o/p:
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""