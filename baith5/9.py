print("đinh văn thiện")
print("235752021610032")
import binary_search

n = int(input("Nhập số lượng phần tử: "))
list = []
print("Nhập các phần tử theo thứ tự tăng dần:")
for i in range(n):
  element = int(input(f"Nhập phần tử thứ {i+1}: "))
  list.append(element)

value = int(input("Nhập giá trị cần tìm: "))

result = binary_search.binary_search(list, value)

if result:
  print("Giá trị đã được tìm thấy")
else:
  print("Giá trị không tìm thấy")
