print("đinh văn thiện")
print("235752021610032")

k=open(r"C:\Users\12\Documents\ZALO\Thịnh\đọc file.py",'r')
char,wc,lc=0,0,0
for line in k:
    for k in range(0,len(line)):
        char +=1
        if(line[k]==' '):
            wc+=1
        if(line[k]=='\n'):
            wc,lc=wc+1,lc+1
print("the no.of chars is %d\n the no.of words is %d\n the no.of lines is %d"%(char,wc,lc))
                
