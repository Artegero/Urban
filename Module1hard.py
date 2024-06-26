grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students_list = sorted(tuple(students))
# print(students_list)  # ['Aaron', 'Bilbo', 'Johnny', 'Khendrik', 'Steve']

score0 = sum(grades[0])/len(grades[0])
score1 = sum(grades[1])/len(grades[1])
score2 = sum(grades[2])/len(grades[2])
score3 = sum(grades[3])/len(grades[3])
score4 = sum(grades[4])/len(grades[4])

# print(score0, score1, score2, score3, score4)
# 4.0 2.25 4.0 3.6666666666666665 4.8

print(dict([[students_list[0], score0],
            [students_list[1], score1],
            [students_list[2], score2],
            [students_list[3], score3],
            [students_list[4], score4]]))