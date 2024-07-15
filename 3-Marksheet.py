# 3.Create a Marksheet for 5 subjects and calculate total, average and grade with if else.
subjects = ["math ", "science ", "english ", "history ", "geography "]
marks = []

for subject in subjects:
    mark = float(input(f"enter the marks for {subject}: "))
    marks.append(mark)

    total = sum (marks)
    average = total / len(subjects)

if average == 90:
    grade = 'a'
elif average >= 80:
    grade = 'b'
elif average >= 70:
    grade = 'c'
elif average >= 60:
    grade = 'd'
elif average >= 50:
    grade = 'f'
else:
    grade = 'g'

print (f"Total marks : {total}")
print (f"Average marks : {average}")
print (f"Grade: {grade}")
