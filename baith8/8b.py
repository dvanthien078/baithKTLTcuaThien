import tkinter as tk
def create_radio_form():
    root = tk.Tk()
    root.title("Form với nút radio")

    selected_value = tk.StringVar()

    # Tạo các nút radio
    radio1 = tk.Radiobutton(root, text="First", variable=selected_value, value="1")
    radio2 = tk.Radiobutton(root, text="Second", variable=selected_value, value="2")
    radio3 = tk.Radiobutton(root, text="Third", variable=selected_value, value="3")

    # Tạo nút "Click Me"
    def click_me():
        print("Bạn đã chọn:", selected_value.get())

    button = tk.Button(root, text="Click Me", command=click_me)

    # Đặt các widget lên giao diện
    radio1.pack()
    radio2.pack()
    radio3.pack()
    button.pack()

    root.mainloop()

# Chọn form muốn hiển thị
create_radio_form()  # Thay đổi thành create_info_form() nếu muốn hiển thị form thông tin cá nhân
