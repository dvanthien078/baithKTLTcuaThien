print("đinh văn thiện")
print("235752021610032")

input_file=open(r"C:\Users\12\Documents\ZALO\Thịnh\đọc file.py",'r')
for line in input_file:
    l=len(line)
    s=' '
    while(l>=1):
        s=s+line[l-1]
        l=l-1
    print(s)
input_file.close()
