import os
import math  # Step 1: Import the math module

path = os.getcwd()
students = {}


def add_student(name, scores): #function used to define name and score
    students[name] = scores

def get_average(scores):
    average = sum(scores) / (len(scores) + 1)
    return math.ceil(average)  # Step 2: Round up the result

#UI
print("Phần mềm nhập điểm\n"
      "1. Nhập điểm\n"
      "2. Xem điểm\n"
      "3. Thoát")
choice = input("Nhập số để chọn: ")

# Nhập điểm
if choice == "1":
    while True :
        a = input("Nhập tên hs hoặc nhập 'stop' để dừng: ")
        if a == "stop":
            break 
        b = int(input("Điểm hệ số 1: "))
        c = int(input("Điểm hệ số 2: "))
        scores = [ b, 2*c]
        add_student( a, scores)
    
 #Hiện điểm TB
    for name, scores in students.items():
        print(name + " Điểm TB (làm tròn): " + str(get_average(scores)))

    print("Có muốn lưu điểm không: ")
    if input("có hay không: ") == "có":
        k = str(input("Tên file: ")) + ".txt"
        with open(k, "w") as f:
            for name, scores in students.items():
                f.write( "Tên hs: " + name + "\nĐiểm hệ số 1: " + str(scores[0]) + "\nĐiểm hệ số 2: " + str(scores[1]/2) + 
                        "\n Điểm TB (làm tròn): " + str(get_average(scores)) +'\n')
    print("Đã lưu!")


# Xem điểm
elif choice == "2":
    files = [f for f in os.listdir() if os.path.isfile(f) and f.endswith(".txt")]
    if not files:
        print("Không có file nào để mở.")
    else:
        print("Các file đã lưu:")
        for i, file in enumerate(files):
            print(f"{i + 1}. {file}")
        selected = int(input("Chọn số file để mở: ")) - 1
        if 0 <= selected <= len(files):
            with open(files[selected], "r") as f:
                print("\nNội dung file:")
                print(f.read())
        else:
            print("Lựa chọn không hợp lệ!")

elif choice == "3":
    print("Đã thoát!")




