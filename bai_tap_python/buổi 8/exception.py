# import sys

# # def exception_1() :
# try:
#   fcovid = open("vd10.txt","r",encoding = "utf - 8")
# except ZeroDivisionError: #IOError là lệnh của trương trình xem có lỗi
#   print("có lỗi mở file")
#   fcovid = open("rem.txt","r",encoding = "utf - 8")
#   a = fcovid.read()
#   print(a)

# except :
#   a = sys.exc_info()
#   print("có lỗi %s"%a[0]," xẩy ra")

# else:
#   pass

# finally :
#   print("rem đã xuất hiện")

# print("rem rem rem")


# def exception_2() :
#   thong_tin = "nam ngoai 1 -> 10"
#   a = int(input("Nhap vao 1 so tu 1 -> 10"))
#   if a < 1 or a > 10:
#       raise Exception(thong_tin)

# def assert_2():
    

# if __name__ == "__main__":
#   exception_2()



# cú pháp
# try:
#   khối lệnh nghi ngờ có lỗi
# except lỗi 1 : nếu xẩy ra lỗi 1 sẽ thực hiện phương án 1
#   Phương án xử lý lỗi 1

# except lỗi 2:
#   phương án xử lý lỗi 2

# except:
# cos looix nhungw ko duwj ddoans ddos laf looix gif

# else:
#   không có lỗi thì sẽ thực thi lệnh trong này

# sys.exc_info() lưu các lỗi xẩy(trả về lỗi đã xẩy ra) ra năm trong thư viện sys
# finally : Finally luôn luôn chạy bất kể có lỗi xảy ra hay không
#   khối lệnh 3


# Tự kích hoạt ngoại lệ
# raise Exception()



# các buit in exception:
# - lỗi vào ra : IOError
# - lỗi chia cho số 0 : ZeroDivisionError
# - lỗi về giá trị : ValueError
# - lỗi import : importError
# - lỗi tên : NameError 


# try:
#   a = int(input("Nhap a: "))
#   b = int(input("Nhap b: "))
#   c = a/b

# except ValueError:
#   print("có lỗi kiểu dữ liệu")
#   print("xin mời nhập lại ")

# except ZeroDivisionError:
#   print("chia cho 0")
#   print("xin mời nhập lại")
# else:
#   print(c)

a = 3 

b = 2

if a>b:
  print(a)

elif a<b:

  print(b)