grades_students = [1,2,3,4.3]
list_range = list(range(1,11))
list_range_steps = list(range(2,9,2))

sum1 = sum(grades_students)
sum2 = sum(list_range)
sum3 = sum(list_range_steps)

print(grades_students, list_range, list_range_steps)
print(sum1, sum2, sum3)
print(sum1/len(grades_students), sum2/len(list_range), sum3/len(list_range_steps))
