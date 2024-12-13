import tkinter as tk

def show_choice():
    selected_language = language.get()
    print(f"Bạn đã chọn: {selected_language}")

root = tk.Tk()
root.title("Chọn Ngôn Ngữ ")  

language = tk.IntVar() 
language.set(1)  # Mặc định chọn English

languages = [
    ("English", 1),
    ("Japanese", 2),
    ("Korean", 3),
    ("Vietnamese", 4),
    ("Chinese", 5)
]

label = tk.Label(root, text="Chọn ngôn ngữ của bạn:", justify=tk.LEFT, padx=20)
label.pack()

for text, value in languages:
    radio_button = tk.Radiobutton(
        root,
        text=text,
        variable=language,
        value=value,
        command=show_choice,
        indicatoron=False, 
        padx=20,
        anchor=tk.W
    )
    radio_button.pack()

root.mainloop()
