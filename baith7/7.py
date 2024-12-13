print("đinh văn thiện")
print("235752021610032")
def count_lines(filename):
  count = 0
  with open(filename, 'r') as f:
    for line in f:
      count += 1
  return count

filename = (r"C:\Users\12\Documents\ZALO\Thịnh\py.py")
total_lines = count_lines(filename)
print("Số dòng trong tệp", filename, "là", total_lines)
