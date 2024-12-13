print("đinh văn thiện")
print("235752021610032")

import numpy as np


data_type = [('name', 'S15'), ('class', int), ('height', float)]

students = np.array([('James', 5, 48.5), ('Nail', 6, 52.5), ('Paul', 5, 42.1), ('Pit', 5, 40.11)],
                     dtype=data_type)

students = np.sort(students, order=['class', 'height'])

print("Danh sách sinh viên sau khi sắp xếp:")
print(students)
