if __name__ == '__main__':
    students = []
    
    # 1. Take input and store in a nested list
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
    # 2. Extract all scores and find the unique second-lowest
    # We use set() to remove duplicates and sorted() to order them
    unique_scores = sorted(set([score for name, score in students]))
    second_lowest_grade = unique_scores[1]
    
    # 3. Get names of students with that grade
    # We filter students and sort the resulting names list
    result_names = sorted([name for name, score in students if score == second_lowest_grade])
    
    # 4. Print each name on a new line
    for name in result_names:
        print(name)