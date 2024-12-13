print('đinh văn thiện mssv 235752021610032')
def find_max_min(numbers):
    n = len(numbers)
    min_index = 0
    max_index = 0
    for i in range(1, n):
        if numbers[i] < numbers[min_index]:
            min_index = i
        elif numbers[i] > numbers[max_index]:
            max_index = i
    return min_index, numbers[min_index], max_index, numbers[max_index]

if __name__ == "__main__":
    n = int(input("Nhập số lượng phần tử: "))
    numbers = []
    for i in range(n):
        number = int(input(f"Nhập phần tử thứ {i+1}: "))
        numbers.append(number)

    min_index, min_number, max_index, max_number = find_max_min(numbers)

    print("Vị trí số nhỏ nhất:", min_index + 1)  
    print("Số nhỏ nhất:", min_number)
    print("Vị trí số lớn nhất:", max_index + 1)
    print("Số lớn nhất:", max_number)
