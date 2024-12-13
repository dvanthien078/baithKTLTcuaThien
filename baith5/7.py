import numpy as np
student_dtype = [('name', 'U20'), ('class', int), ('height', float), ('data_type', 'U10')]

students_data = [
    ('Đinh Văn Thiện', 10, 1.75, 'Sinh học'),
    ('Nguyễn Quang Trung', 11, 1.65, 'Toán'),
    ('Hoàng Đình Trường', 10, 1.80, 'Lý')
]

students = np.array(students_data, dtype=student_dtype)
print("Danh sách sinh viên ban đầu:")
print(students)
print("\nDanh sách sinh viên sau khi sắp xếp theo chiều cao:")
students_sorted_by_height = np.sort(students, order='height')
print(students_sorted_by_height)
print("\nDanh sách sinh viên sau khi sắp xếp theo lớp và chiều cao:")
students_sorted_by_class_and_height = np.sort(students, order=['class', 'height'])
print(students_sorted_by_class_and_height)

