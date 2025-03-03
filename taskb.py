def convert_grade(grade):
    
    if 80 <= grade <= 100:
        return 'A'
    elif 60 <= grade <= 79:
        return 'B'
    elif 50 <= grade <= 59:
        return 'C'
    elif 40 <= grade <= 49:
        return 'D'
    elif 0 <= grade <= 39:
        return 'F'
    else:
        return None

try:
    grade_input = input("Enter your grade (0-100): ")

    grade = float(grade_input)

    if grade < 0 or grade > 100:
        print("Error: Grades must be between 0 and 100")
    else:
        letter_grade = convert_grade(grade)
        print(f"Your grade is: {letter_grade}")

except ValueError:
    print("Error: Please enter a number")
