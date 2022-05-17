from gtts import gTTS
from playsound import playsound
import datetime
from datetime import date


k = int(input("nhap so nguyen n: "))
s = 0
tu = 0

for i in range(1, +1):
	tu = (i+1)/i 
	s = s + tu

print(s+1)

miku = [z for z in range(999)]
i = 0
temp = 0
number = 0
nguyen_to = 0
sum_nguyen_to = 0

print("nhap n:") 
n = int(input())

for i in range(0,n):
	print(end="nhap so thu %d: "%(i+1))
	miku[i] = int(input())	

for i in range(0,n+1):
	for j in range(i+1,n):
		if miku[i] < miku[j]:
			temp = miku[i]
			miku[i] = miku[j]
			miku[j] = temp

print("so lon nhat la: %d"%(miku[0]))
print("so lon nhi la: %d"%(miku[1]))

number = 0
for i in range(0,n):
	if miku[i] != miku[n-1-i]:
		number +=1

if number >= 1:
	print("ko doi xung")

else :
	print("doi xung")

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

print("nhap bien x")
x_them = int(input())
print("so lon hon x la: ")
for i in range(0,n):
	if miku[i] > x_them:
		print(end="%d  "%(miku[i]))

print("\ntang dan:")

for i in range(1,4+1):
	print(end="%d "%miku[i-1])	



SoTuNhien = ['không', 'một', 'hai', 'ba', 'bốn', 'năm', 'sáu', 'bảy', 'tám', 'chín']
DonVi = ['mươi', 'mốt', 'hai', 'ba', 'bốn', 'lăm', 'sáu', 'bảy', 'tám', 'chín']
#Chuc = ['linh', 'mười', 'hai', 'ba', 'bốn', 'lăm', 'sáu', 'bảy', 'tám', 'chín']
phan_khuc = ['',' nghìn ', ' triệu ', ' tỷ ', ' nghìn tỷ ', 'triệu tỷ']
#Cum = ['trăm', 'chục', 'đơn vị']


def chia_phan_khuc(a):
    n = a
    phan_khuc = []
    while n > 0:
        phan_khuc.append(int(n % 1000))
        n = int(n / 1000)
    return phan_khuc


def doc_so_chuc(a):
    if a == 10:
        return "mười"
    elif int(a % 10) == 0:
        return SoTuNhien[int(a/10)] + " " + "mươi"
    elif a < 20:
        return "mười " + SoTuNhien[int(a % 10)]
    else:
        return SoTuNhien[int(a/10)] + " mươi " + DonVi[int(a % 10)]


def doc_so_tram(a):
    if a < 10:
        return "không trăm linh " + SoTuNhien[a]
    elif a < 99:
        return "không trăm " + doc_so_chuc(a)
    elif a % 100 == 0:
        return SoTuNhien[int(a/100)] + " trăm"
    elif a % 100 < 10:
        return SoTuNhien[int(a/100)] + "trăm linh " + SoTuNhien[int(a % 100)]
    else:
        return SoTuNhien[int(a/100)] + " trăm " + doc_so_chuc(int(a % 100))


S = ''
a = int(input("Nhập số cần đọc: "))
phan_khuc = chia_phan_khuc(a)
if len(phan_khuc) == 1:
    if a < 10:
        S = SoTuNhien[a]
    elif a < 99:
        S = doc_so_chuc(a)
    else:
        S = doc_so_tram(a)
else:
    for i in range(len(phan_khuc)-1):
        if phan_khuc[i] == 0:
            continue
        else:
            S = doc_so_tram(phan_khuc[i]) + phan_khuc[i] + S
    else:
        b = phan_khuc[len(phan_khuc) - 1]
        if b < 10:
            S = SoTuNhien[b] + phan_khuc[len(phan_khuc) - 1] + S
        elif b < 99:
            S = doc_so_chuc(b) + phan_khuc[len(phan_khuc) - 1] + S
        else:
            S = doc_so_tram(b) + phan_khuc[len(phan_khuc) - 1] + S
print(S)
tts = gTTS(S, tld='com.vn', lang='vi')
tts.save("hello.mp3")
playsound("hello.mp3")



