from src.is_triangle import is_triangle

def main():
    a = float(input("Nhập độ dài cạnh a: "))
    b = float(input("Nhập độ dài cạnh b: "))
    c = float(input("Nhập độ dài cạnh c: "))
    if is_triangle(a, b, c):
        print("Ba cạnh a, b, c tạo thành một tam giác.")
    else:
        print("Ba cạnh a, b, c không tạo thành một tam giác.")

if __name__ == '__main__':
    main()
