print("đinh văn thiện")
print("235752021610114")
def copy_file_loop(source_file, destination_file):

  with open(source_file, 'r') as f_in, open(destination_file, 'w') as f_out:
    for line in f_in:
      f_out.write(line)

source = (r"C:\Users\12\Documents\ZALO\Thịnh\file1.py")
destination = (r"C:\Users\12\Documents\ZALO\Thịnh\file2.py")
copy_file_loop(source, destination)

