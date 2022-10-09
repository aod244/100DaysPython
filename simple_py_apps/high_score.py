student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

max_score = 0
min_score = 100
for student_score in student_scores:
    if student_score > max_score:
        max_score = student_score
    if student_score < min_score:
        min_score = student_score
    
print(student_scores)
print(f"The highest score in class is: {max_score}")
print(f"The lowest score in class is: {min_score}")