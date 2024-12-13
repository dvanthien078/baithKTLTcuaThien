print('đinh văn thiện mssv 235752021610032')
import tkinter as tk

languages = {
    '1': 'English',
    '2': 'Japanese',
    '3': 'Korean',
    '4': 'Tiếng Việt',
    '5': 'Chinese'
}

def show_choice():
    print(f"Ngôn ngữ bạn chọn là: {v.get()}")

root = tk.Tk()
root.title("Chọn ngôn ngữ:")

v = tk.IntVar()
for i, language_code in enumerate(['1', '2', '3', '4', '5']):
    tk.Checkbutton(root,
                   text=languages[language_code],
                   variable=v,
                   command=show_choice,
                   onvalue=i+1,
                   indicatoron=1).pack(anchor=tk.W)

root.mainloop()
