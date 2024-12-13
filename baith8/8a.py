import tkinter as tk

def ho_va_ten():
    print('đinh văn thiện')

def ngay_thang_nam_sinh():
    print('07/08/2004')
    
def mssv():
    print('235752021610032')

def nghanh_hoc():
    print('KTĐK&TĐH')


window = tk.Tk()
window.title('Chương trình graphic')

menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

thongtin_menu = tk.Menu(menu_bar, tearoff=0)
thongtin_menu.add_command(label='họ và tên',command=ho_va_ten)
thongtin_menu.add_command(label='ngày tháng năm sinh',command=ngay_thang_nam_sinh)
thongtin_menu.add_command(label='MSSV', command=mssv)
thongtin_menu.add_command(label='Nghành học',command=nghanh_hoc)
thongtin_menu.add_separator()
thongtin_menu.add_command(label="Thoát", command=window.quit)
menu_bar.add_cascade(label="Thông tin", menu=thongtin_menu)
window.mainloop()
