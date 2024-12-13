print("đinh văn thiện")
print("235752021610032")

def doc_toan_bo_file(ten_file):

  with open(ten_file, 'r') as file:
    noi_dung = file.read()
  return noi_dung


ten_file = (r"C:\Users\12\Documents\ZALO\Thịnh\đọc file.py")
noi_dung = doc_toan_bo_file(ten_file)

print(noi_dung)
