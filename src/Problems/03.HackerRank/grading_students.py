# https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true


def gradingStudents(grades):
    # Write your code here
    for index in range(len(grades)):
        quotient = grades[index] // 5  # Find how many times 5 fits into the grade
        next_multiple_of_five = (quotient + 1) * 5  # Calculate the next multiple of 5
    
        # Check if the grade should be rounded
        if (next_multiple_of_five - grades[index]) < 3 and grades[index] >= 38:
            grades[index] = next_multiple_of_five  # Round up the grade
            print(grades[index])

    return grades


gradingStudents([73, 67, 38, 33, 57, 29])


"""
    Student 1 received a 73, and the next multiple of 5 from 73 is 75. Since 75 - 73 < 3, the student's grade is rounded to 75.
    Student 2 received a 67, and the next multiple of 5 from 67 is 70. Since 70 - 67 = 3, the grade will not be modified and the student's final grade is .
    Student 3 received a 38, and the next multiple of 5 from 38 is 40. Since 40 - 38 < 3, the student's grade will be rounded to 40.
    Student 4 received a 33, grade below 33, so the grade will not be modified and the student's final grade is 33.
"""