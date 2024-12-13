import tkinter as tk
print('đinh văn thiện msv 235752021610032')

def open_file():
    print("Mở file")

def save_file():
    print("Lưu file")
def new_file():
    print("File mới")
def undo_edit():
    print('hoàn tác')
def redo_edit():
    print('làm lại')
def selectall_edit():
    print('chọn tất cả')
def run_run():
    print('chạy file')
    

window = tk.Tk()
window.title("Cửa Sổ Của Làm Việc của Thiện")

menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Mở", command=open_file)
file_menu.add_command(label="Lưu", command=save_file)
file_menu.add_command(label="file mới", command=new_file)
file_menu.add_separator()
file_menu.add_command(label="Thoát", command=window.quit)
###
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label='Undo', command=undo_edit)
edit_menu.add_command(label='Redo', command=redo_edit)
edit_menu.add_command(label='Select all', command=selectall_edit)
###
run_menu = tk.Menu(menu_bar, tearoff=0)
run_menu.add_command(label='Run file', command=run_run)
###
menu_bar.add_cascade(label="File", menu=file_menu)#
menu_bar.add_cascade(label="Edit", menu=edit_menu)#
menu_bar.add_cascade(label="Run", menu=run_menu)#
run_menu = tk.Menu(menu_bar, tearoff=0)
window.mainloop()
