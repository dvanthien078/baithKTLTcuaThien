print("đinh văn thiện")
print("msv 235752021610032")
class StringManipulation:
    def __init__(self):
        self.string = ""

    def get_string(self):
        self.string = input("Nhập chuỗi: ")

    def print_string(self):
        print(self.string.upper())

obj = StringManipulation()

obj.get_string()

obj.print_string()
