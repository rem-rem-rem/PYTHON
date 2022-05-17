def in_name():
	return input("ghi ten ban di: ")

def chuan_hoa(name:str):
	len_name = len(name)
	rem = []
	for i in range(len_name):
		rem.append(0)

	for i in range(len_name):
		rem[i] = ord(name[i])

	for i in range(len_name):
		if rem[i] > 65 and rem[i] < 90:
			rem[i] = rem[i] + 32
			rem[i] = chr(rem[i])
		else:
			rem[i] = chr(rem[i])

	return rem

def ghi_hoa(name:str):
	rem = chuan_hoa(name)
	k = []

	for j in range(len(name)):
		k.append(rem[j])
		k[j] = ord(k[j])

	for i in range(len(name)):
		rem[i] = ord(name[i])

	for i in range(len(name)):

		if rem[i] == 32:
			k[i+1] = k[i+1] - 32

		elif i == 0:
			k[i] = k[i] - 32

		k[i] = chr(k[i])
		print(k[i])
	return k	 

def xuat_ten(name:str):
	rem = ghi_hoa(name)
	for i in range(len(name)):
		print("%s"%rem[i])

def xuat_tung_chu(name:str):
	rem = chuan_hoa(name)

	for i in range(len(name)):
		rem[i] = ord(name[i])

	for i in range(len(name)):
		if rem[i] == 32:
			rem[i] = chr(rem[i])
			print("\n")

		else:
			rem[i] = chr(rem[i])
			print(end="%s"%rem[i])

def xuat_tung_ki_tu(name:str):
	rem = ghi_hoa(name)

	for i in range(len(rem)):
		rem[i] = ord(rem[i])

	for i in range(len(rem)):
		if rem[i] == 32:
			rem[i] = chr(rem[i])
			print("\n")

		else:
			rem[i] = chr(rem[i])
			print(end="%s"%rem[i])

def xuat_tung_chu_dao(name:str):
	namem = name
	s = namem.title()
	rem_1 = s.split(" ")
	a = []

	for i in range(len(rem_1)):
		if(rem_1[i] != ""):
			a.append(rem_1[i])

	for i in range(len(a)-1, -1, -1):
		print(a[i])

def xuat_tung_chu_ho_ten(name:str):
	namem = name
	s = namem.title()
	rem_1 = s.split(" ")
	a = []

	for i in range(len(rem_1)):
		if(rem_1[i] != ""):
			print(rem_1[i])
			a.append(rem_1[i])

	print("Ho: ",a[0])
	print("ten lot: ", end="")
	for i in range(1, len(a) - 1):
		print(a[i], end=" ")

	print("")

	print("Ten: ", a[len(a) - 1])

	print(a)



if __name__ == "__main__":

	running = 1
	name = in_name()

	while (running == 1):
		print("\nnhập 1 để chuẩn hóa và ghi hoa kí tự đầu ")
		print("nhập 2 để xuất từng kí tự lên tùng dòng ")
		print("nhập 3 để xuất từng chữ lên tùng dòng ")
		print("nhập 4 để xuất từng chữ lên tùng dòng chìu đảo ")
		print("nhập 5 để xuất từng chữ theo học tên tên đệm ")
		print("nhập 0 để ")
		rem = int(input("nhap: "))

		if rem == 1 :
			ghi_hoa(name)

		if rem == 2:
			xuat_ten(name)

		if rem == 3:
			xuat_tung_chu(name)

		if rem == 4:
			xuat_tung_chu_dao(name)

		if rem == 5:
			xuat_tung_chu_ho_ten(name)
		if rem == 0 :
			running = 0

	