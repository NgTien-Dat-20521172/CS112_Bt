from src.print_prime import print_prime

if __name__ == "__main__":
    n = int(input("Nhập giá trị n: "))
    print("Danh sách các số nguyên tố trong phạm vi từ 2 đến", n, "là:")
    print(print_prime(n))
