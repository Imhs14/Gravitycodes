'''size = 3
letters = string.ascii_letters[:size]

x = '-'.join(letters[1:])
y = '-'.join(letters[::-1])
z = y + '-' + x
print(z)'''
import string

size = 3
letters = string.ascii_lowercase[:size]  # 'abc'
lines_list = []

# Loop to build each row's characters
for i in range(size):
    # Slice the letters we need for this specific row
    # As i grows, we take fewer letters from the front
    left_part = letters[i:][::-1]  # Decreasing part (e.g., 'cba')
    right_part = letters[i+1:]     # Increasing part (e.g., 'bc')
    
    row_letters = left_part + right_part
    
    # Center the letters with hyphens and add to our list
    width = 4 * size - 3
    centered_row = "-".join(row_letters).center(width, "-")
    
    lines_list.append(centered_row)
    
# Right now, lines_list contains the top half + middle line.
# You can now print them, and then print the top half in reverse!