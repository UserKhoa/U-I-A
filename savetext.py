import os

# UI
print("1. Tạo file mới\n"
      "2. Mở file đã tạo\n"
      "3. Thoát")

choice = input("Chọn 1, 2 hoặc 3: ")

if choice == "1":
    k = str(input("Tên file: "))
    with open(k, "w") as f:
        f.write(input("Ghi nội dung vào file: "))
    print("Đã lưu!\n" + os.path.join(os.getcwd(), k))

elif choice == "2":
    files = [f for f in os.listdir() if os.path.isfile(f) and f.endswith(".txt")]
    
    if not files:
        print("Không có file nào để mở.")
    else:
        print("Các file đã lưu:")
        for i, file in enumerate(files):
            print(f"{i + 1}. {file}")
        
        selected = int(input("Chọn số file để mở: ")) - 1
        if 0 <= selected < len(files):
            with open(files[selected], "r") as f:
                print("\nNội dung file:")
                print(f.read())
        else:
            print("Lựa chọn không hợp lệ.")

elif choice == "3":
    print("Đã thoát.")
else:
    print("Lựa chọn không hợp lệ.")
