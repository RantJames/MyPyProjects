def print_percent(query, student_marks):
    total = 0
    avg = 0
    marks = student_marks.get(query)
    #print(marks)
    for score in marks:
        total = total + score
    avg = total / 300
    print("{:.2f}".format(avg*100))



student_marks = {"John": (10, 20, 30), "Rubin": (20, 30, 40)}
query = 'Rubin'
print_percent(query, student_marks)
