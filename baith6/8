print("đinh văn thiện")
print("235752021610032")
class ATM:
    def __init__(self, name, account_number, balance, pin):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.pin = pin

    def authenticate(self):
        while True:
            pin = input("Nhập mã PIN: ")
            if pin == self.pin:
                return True
            else:
                print("Mã PIN không đúng. Vui lòng thử lại.")

    def menu(self):
        while True:
            print("\nChọn chức năng:")
            print("1. Kiểm tra số dư")
            print("2. Rút tiền")
            print("3. Gửi tiền")
            print("4. Thoát")
            choice = int(input())
            if choice == 1:
                print(f"Số dư hiện tại: {self.balance}")
            elif choice == 2:
                amount = int(input("Nhập số tiền muốn rút: "))
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"Rút tiền thành công. Số dư còn lại: {self.balance}")
                else:
                    print("Số dư không đủ")
            elif choice == 3:
                amount = int(input("Nhập số tiền muốn gửi: "))
                self.balance += amount
                print(f"Gửi tiền thành công. Số dư mới: {self.balance}")
            elif choice == 4:
                break
            else:
                print("Lựa chọn không hợp lệ.")

account = ATM("đinh văn thiện", "235752021610032", 500.000, "0708")

account.authenticate()

account.menu()
