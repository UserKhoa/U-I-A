print("làm tý toán không?")

question = ["1+1=?","3!=?", "13*8=?", "27:3=?", "28+10:5=?"]
answer = ["2", "6", "104", "9", "30"]
index = 0
	
if input("có hay không: ") == "có":
    while True:
        if index >= len(question):
            print("tốt lắm! Hết bài rồi!")
            break

        print(question[index])
        if input("Đáp án: ") == answer[index]:
            print("tốt!")
            index += 1
        else:
            print("buồn rồi")
            break


