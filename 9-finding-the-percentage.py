"""
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.
 Print the average of the marks array for the student name provided, showing 2 places after the decimal.
"""
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    list_of_scores = student_marks[query_name]
    numerator = sum(list_of_scores)
    denominator = len(list_of_scores)
    result = numerator/denominator
    print(f"{result:.2f}")

"""
example i/p & o/p
4 
a 90 86 90 09
b 08 98 67 86
c 87 98 65 78
d 78 56 98 76
d
77.00
"""