import math
import os
import random
import re
import sys
def missingCharacters(s):
    c = 'abcdefghijklmnopqrstuvwxyz'
    n = '0123456789'
    
    # Using a set makes looking up characters much faster
    present_chars = set(s)
    result = ""
    # 1. Find and append missing digits first
    for digit in n:
        if digit not in present_chars:
            result += digit
            
    # 2. Find and append missing letters second
    for letter in c:
        if letter not in present_chars:
            result += letter
            
    return result

if __name__ == '__main__':
    s = input()
    result = missingCharacters(s)
    print(result)