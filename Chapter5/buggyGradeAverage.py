#debug the program and find the issue to fix the problem with the result
#exercise 2 zero division error: fix so that the code doesn't crash when the user hasnt entered anything and instead returns zero
def calculate_grade_average(grade_sum, number_of_grades):
    #exercise 2 result is ther added if statement to account for not entering anything
    if number_of_grades == 0:
        return 0
    grade_average = int(grade_sum / number_of_grades)
    return grade_average

counter = 0
total = 0
while True:
    print('Enter a grade, or "done" if done entering grades:')
    grade = input()
    if grade == 'done':
        break
    counter = counter + 1
    total = total + int(grade)

#original problem was that total and counter were swapped making it always result in 0 
avg = calculate_grade_average(total, counter)
print('The grade average is:', avg)