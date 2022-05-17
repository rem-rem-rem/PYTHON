'''
Created on 9 thg 4, 2022

@author: A315-56
'''
# BÀI TẬP TUẦN 8
# Bài 2: Nhập 2 số a, b. Tính hiệu a/b. Yêu cầu xử lý trường hợp ngoại lệ (bắt riêng):
# a) Vô tình nhập chuỗi không phải số. (không cần kiểm tra chuỗi nhập là số hay không)
# b)Vô tình nhập b=0. (không cần kiểm tra if(b==0) )


import sys
a = 0
b = 0

try:
    a = int(input("Nhập số a:"));
except ValueError:   
    print("Vui lòng nhập số, không nhập ký tự!")
    sys.exit()
    
try:
    b = int(input("Nhập số b:"));
    c = a/b
except ZeroDivisionError:   
    print("Vui lòng nhập số khác 0!")
    sys.exit()   
except ValueError:   
    print("Vui lòng nhập số, không nhập ký tự!")
    sys.exit()


d = a/b
print(d)
