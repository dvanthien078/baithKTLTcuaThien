print('đinh văn thiện msv 235752021610032')
def read_last_n_lines(file_path, n):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            if n > len(lines):
                print(f"Tệp chỉ có {len(lines)} dòng.")
            else:
                for line in lines[-n:]:
                    print(line.strip())
    except FileNotFoundError:
        print(f"Không tìm thấy tệp: {file_path}")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Ví dụ sử dụng
file_path = r"C:\Users\12\Documents\ZALO\Thịnh\py.py"
n = 3
read_last_n_lines(file_path, n)
