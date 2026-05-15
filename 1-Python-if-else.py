inpt = int(input(""))
if inpt%2 != 0 or (inpt>=6 and inpt<=20):
    print("Weird")
elif (inpt>=2 and inpt<=5) or (inpt>20):
    print("Not Weird")


"""Given an integer,n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
"""