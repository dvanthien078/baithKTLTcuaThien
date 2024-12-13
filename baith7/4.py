print('đinh văn thiện msv 235752021610032')
def read_first_n_lines(filename, n):
    try:
        with open(r'C:\Users\12\Documents\ZALO\Thịnh\py.py', encoding='utf-8') as file:
            for i in range(n):
                line = file.readline()
                if line:  
                    print(line.strip())  
                else:
                    break 
    except FileNotFoundError:
        print(f"File {filename} không tồn tại.")
filename = r"C:\Users\12\Documents\ZALO\Thịnh\py.py" 
n = 4
read_first_n_lines(filename, n)
