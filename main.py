grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = sorted(list(students))
a = sum(grades[0])/len(grades[0])
b = sum(grades[1])/len(grades[1])
c = sum(grades[2])/len(grades[2])
d = sum(grades[3])/len(grades[3])
e = sum(grades[4])/len(grades[4])
average_list = [(a),(b),(c),(d),(e)]
average_grades = dict(zip(students_list, average_list))
print(average_grades)