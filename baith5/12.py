print("đinh văn thiện")
print("235752021610032")
import numpy as np

student_id = [1023, 5202, 6230, 1671, 1682, 5241, 4532]
student_height = [40., 42., 45., 41., 38., 40., 42.0]

data = np.array([student_id, student_height]).T


indices = np.lexsort((data[:, 1],))  
print("Chỉ số:")
print(indices)

print("Dữ liệu sắp xếp:")
for i in indices:
    print(data[i])
