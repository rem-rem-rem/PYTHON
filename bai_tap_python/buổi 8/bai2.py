
import sys

a = 0
in_number = []
tong = 0
tich = 1
# Nhập n số rồi lưu vào file input.txt
file_name = "input.txt"
n = int(input("Nhập số giá trị n: "))

for i in range(n):  
    try:
        a = int(input("Nhập số thứ " + str(i+1) + ": "));
        c = 5/a
    except ZeroDivisionError:   
        print("Vui lòng nhập số khác 0!")
        sys.exit()   
    except ValueError:   
        print("Vui lòng nhập số, không nhập ký tự!")
        sys.exit()
    else: 
        in_number.append(a)
 
#Mở file ra và ghi   
input_file = open(file_name, "w", encoding = "utf-8") 
  
for i in in_number:   
    input_file.write(str(i) + "\n")
    
print("Đã ghi giá trị vào file " + file_name)
input_file.close() 

# Đọc 2 số a và b từ file input.txt, tính a+b, a*b
input_file = open(file_name, "r", encoding = "utf-8")
for i in range(n): 
    data = input_file.readline()
    tong = tong + int(data)
    tich = tich * int(data)

print("Tong = " + str(tong))
print("Tich = " + str(tich))

input_file.close() 

# Lưu vào file kq.txt
input_file = open("kq.txt", "w", encoding = "utf-8")    
input_file.write(str(tong) + "\n")
input_file.write(str(tich) + "\n")
print("Đã ghi kết quả vào file kq.txt \n")
input_file.close() 






