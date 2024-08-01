grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

our_students_ = sorted(students)

Fellas = {}

Fellas.update({our_students_[0]: sum(grades[0]) / len(grades[0]),
               our_students_[1]: sum(grades[1]) / len(grades[1]),
               our_students_[2]: sum(grades[2]) / len(grades[2]),
               our_students_[3]: sum(grades[3]) / len(grades[3]),
               our_students_[4]: sum(grades[4]) / len(grades[4])})

print(Fellas)