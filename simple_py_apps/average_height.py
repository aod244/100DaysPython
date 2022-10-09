from operator import index, indexOf


student_heights = input("Input a list of student heights ").split()
sum_heights = 0
num_students = 0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(f"The heights of students are: {student_heights}")
for student_height in student_heights:
    sum_heights = sum_heights + student_height
    num_students = num_students + 1

print(f"Average height of students is {round(sum_heights/num_students)}")
