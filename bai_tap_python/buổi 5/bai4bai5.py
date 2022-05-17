import string

def tai_khoan():
	LA = list(string.ascii_lowercase)
	UA = list(string.ascii_uppercase)
	Num = list(string.digits)
	symboy = ['$', '#', '@']
	password = list(str(input("Nhap mat khau moi yeu cau phai co it nhat 1 ki tu trong khoang a-z  yeu cau phai co it nhat 1 ki tu trong khoang A-Z yeu cau phai co it nhat 1 so trong khoang 0-9 yeu cau phai co it nhat 1 ki tu thuoc [$ # @] do dai yeu cau nam trong khoang 6-12: ")))
	if(len(password) > 5 and len(password) < 13):
	    for i in password:
	        tmp = 0
	        for j in LA:
	            if(i == j):
	                tmp = 1
	                break
	        if(tmp == 1):
	            break
	    else:
	        print("Mat khau khong hop le, yeu cau phai co it nhat 1 ki tu trong khoang a-z !")
	        exit(0)
	    for i in password:
	        tmp = 0
	        for j in UA:
	            if(i == j):
	                tmp = 1
	                break
	        if(tmp == 1):
	            break
	    else:
	        print("Mat khau khong hop le, yeu cau phai co it nhat 1 ki tu trong khoang A-Z !")
	        exit(0)
	    for i in password:
	        tmp = 0
	        for j in Num:
	            if(i == j):
	                tmp = 1
	                break
	        if(tmp == 1):
	            break
	    else:
	        print("Mat khau khong hop le, yeu cau phai co it nhat 1 so trong khoang 0-9 !")
	        exit(0)
	    for i in password:
	        tmp = 0
	        for j in symboy:
	            if(i == j):
	                tmp = 1
	                break
	        if(tmp == 1):
	            break
	    else:
	        print("Mat khau khong hop le, yeu cau phai co it nhat 1 ki tu thuoc [$ # @] !")
	        exit(0)
	    print("Mat khau hop le!")
	else:
	    print("Do dai mat khau khong hop le, yeu cau nam trong khoang 6-12")


if __name__ == '__main__':
	print("giao dien goi nuoc")
	print("")
	a = "Theater: AMC25 at SAN JOSE, CA"
	print(a.center(32))
	b = 28*"*"
	print("")
	print(b.center(32))
	c = '||{:^28}||'.format('WELCOME  TO')
	print(c)
	d = '||{:^28}||'.format('AMC 25')
	print(d)
	print(b.center(32))
	print("")
	e = "Simple Movie Theater System"
	print(e.center(32))
	f = 27*"="
	print(f.center(32))
	print(" 1--> View all movies")
	print(" 2--> Search a movie")
	print(" 3--> Purchase tickes")
	print(" 4--> Quit")
	print("")
	print(" Please select an option:")
	print("")
	print("==============================================================================================================")


	print("=====================tai khoan ====================")

	tai_khoan()