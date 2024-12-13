print('đinh văn thiện mssv 235752021610032')
def find_max_min(numbers):
  sorted_numbers = sorted(numbers)
  return sorted_numbers[0], sorted_numbers[-1]

if __name__ == "__main__":
  n = int(input("Nhập số lượng phần tử: "))
  numbers = []
  for i in range(n):
    number = int(input(f"Nhập phần tử thứ {i+1}: "))
    numbers.append(number)

  min_number, max_number = find_max_min(numbers)

  print("Phần tử nhỏ nhất:", min_number)
  print("Phần tử lớn nhất:", max_number)
