print("đinh văn thiện")
print("235752021610032")
def write_list_to_file(list_data, filename):
  with open(filename, 'w') as f:
    for item in list_data:
      f.write(str(item) + '\n')
my_list = [1, 2, 3, "hello", "world"]
output_file = (r"C:\Users\12\Documents\ZALO\Thịnh\docfilepython.py")

write_list_to_file(my_list, output_file)
print("Danh sách đã được ghi vào tệp", output_file)
