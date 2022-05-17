
running = 1
key = ['a', 'b', "c", "d","e","f","g","h","i","j","k","l","m","n"]

while running == 1:
	
	# key = delete('Thang',key,value)
	print("\n1 de add")
	print("2 de delete\n")
	print(key)
	i = int(input())
	
	if i == 1:
		add = input("them ki tu:")
		key.append(add)

	if i == 2:
		miku = int(input("nhap vi tri muon xoa() > 0) :"))
		del key[miku - 1]

	if i == 3:
		tai_khoan()

	if i == 0:
		running = 0