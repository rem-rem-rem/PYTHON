def xap_xep_max(n, miku):

	for i in range(0,n+1):
		for j in range(i+1,n):
			if miku[i] < miku[j]:
				temp = miku[i]
				miku[i] = miku[j]
				miku[j] = temp

	print("so lon nhat la: %d"%(miku[0]))
	
def xap_xep_max2(n, miku):
	print("so lon nhi la: %d"%(miku[1]))

def kiem_tra_mang_doi_xung(n, miku):
	number = 0
	for i in range(0,n):
		if miku[i] != miku[n-1-i]:
			number +=1

	if number >= 1:
		print("ko doi xung")

	else :
		print("doi xung")	

def tong_so_nguyen_to(n, miku):
	dem = 0
	sum_nguyen_to = 0
	for j in range(1, n+1):
		for i in range(1, miku[j-1]):
			if miku[j-1] / i == 1:
				dem = dem + 1

		if dem <= 2:
			sum_nguyen_to = sum_nguyen_to + miku[j-1]
			dem = 0
		elif dem > 2:
			dem = 0	
		
	print("tong so nguyen to la %d"%(sum_nguyen_to))


def nhap_x(n, miku):
	print("nhap bien x")
	x_them = int(input())
	print("so lon hon x la: ")
	for i in range(0,n):
		if miku[i] > x_them:
			print(end="%d  "%(miku[i]))

def tang_dan(n, miku):
	for i in range(0,n-1):
		for j in range(i+1,n):
			if miku[i] < miku[j]:
				temp = miku[i]
				miku[i] = miku[j]
				miku[j] = temp
	for i in range(0,n):
		print(end = "%d  "%(miku[n-i]))


if __name__ == "__main__":
	i = 0
	temp = 0
	number = 0
	nguyen_to = 0
	sum_nguyen_to = 0
	running = 1
	miku = [z for z in range(999)]

	print("nhap n:") 
	k = int(input())

	for i in range(0,k):
		print(end="nhap so thu %d: "%(i+1))
		miku[i] = int(input())		
	while (running):

		print("=================================================")
		print("=          nhap so 1 de tinh so lon nhat        =")
		print("=          nhap so 2 de tinh so lon nhi         =")
		print("=      nhap so 3 de kiem tra mang doi xung      =")
		print("=       nhap so 4 de tinh tong so nguyen to     =")
		print("=        nhap so 5 x de tinh so lon hon x       =")
		print("=       nhap so 6 de sap xep mang tang dan      =")
		print("=================================================")

		dieu_kien = int(input())

		if dieu_kien == 1:
			xap_xep_max(k, miku)

		elif dieu_kien == 2:
			xap_xep_max2(k, miku)

		elif dieu_kien == 3:
			kiem_tra_mang_doi_xung(k, miku)

		elif dieu_kien == 4:
			tong_so_nguyen_to(k, miku)

		elif dieu_kien == 5:
			nhap_x(k, miku)

		elif dieu_kien == 6:
			tang_dan(k, miku)

		elif dieu_kien == 0:
			running = 0 

# ten = str(input())
# ten_int = len(ten)
# intt = int(ten_int)

# print(intt)

# print(ten.title())

# for i in range(0,intt):
# 	print(ten[i])

# for i in range(0,intt):
# 	print(end="%s"%ten[i])
# 	if ten[i] == " ":
# 		print("") 

# print("")

# for i in range(1, intt):
# 	print(end="%s"%ten[intt - i])
# 	if ten[i] == " ":
# 		print("")


# print("ho          ten_lot       ten")
# for i in range(0,intt):
# 	print(end="%s"%ten[i])
# 	if ten[i] == " ":
# 		print("         ")	

# print("Nhap ten can sua: ")

# rem = []

# name = input()

# a = int(len(name))

# for i in range(a):
# 	rem.append(i)
# 	rem[i] = name[i]
# yoshino = 0

# for i in range(a):
# 	if(rem[i] == " " and rem[i-1] == " "):
# 		a = a -1

# for i in range(a):
# 	if(rem[i] == " " and rem[i-1] == " "):
# 		del rem[i]

# 	print(end="%s"%rem[i])


# def NAME_Init():
# 	print("Nhập tên cần sửa:")
# 	name = input()
# 	print("Tên của bạn là :", name)
# 	rem = int(len(name))
# 	print("len = %d "%rem)
# 	for i in range(rem):
# 		if(name[i] == " " and name[i-1] == " "):
# 			rem = rem -1
# 	for i in range(rem):
# 		if(name[i] == " "and name[i-1] == " "):
# 			del  name[i]
		
# 		print(end="%s"%name[i])

# 	return 0 

# if __name__ == "__main__":
# 	NAME_Init()
# 	print("\n")


# try:
# 	fcovid = open("vd10.txt","r",encoding = "urf - 8")
# except IOError:
# 	print("co loi mo file")

# else:
# 	a = fcobid.read()
# 	print(a)

# print("rem rem rem")