"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains . The second line contains an array A[ ]  of n integers each separated by a space.
"""

n = int(input(""))

#1. Convert map to a list so we can work with it

#2. Ure set() to remove duplicates (so the runner-up isn't just a tied winner)

#3. Sort the unique scores

arr = list(map(int, input().split()))

unique_scores = sorted(list(set(arr)))

#The runner-up is the second to lastment in the sorted unique Vist

print(unique_scores[-2])