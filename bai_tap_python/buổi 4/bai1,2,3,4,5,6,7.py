import math

def giaiPTBac2(a, b, c):
    if (a == 0):
        if (b == 0):
            print ("Phương trình vô nghiệm!");
        else:
            print ("Phương trình một nghiệm kép : x = ", + (-c / b));
        return;

    delta = b * b - 4 * a * c;

    if (delta > 0):
        x1 = (float)((-b + math.sqrt(delta)) / (2 * a));
        x2 = (float)((-b - math.sqrt(delta)) / (2 * a));
        print ("Phương trình 2 nghiệm : x1 = ", x1, " và x2 = ", x2);
    elif (delta == 0):
        x1 = (-b / (2 * a));
        print("Phương trình có nghiệm kép: x1 = x2 = ", x1);
    else:
        print("Phương trình vô nghiệm!");



print("Chương trình tính điểm trung bình của học sinh")

kiem_tra = 0; giua_ky = 0; cuoi_ky = 0
def nhap_diem():

    print("Nhập điểm kiểm tra: ")
    kiem_tra = float(input())

    print("Nhập điểm giữa kỳ: ")
    giua_ky = float(input())

    print("Nhập điểm cuối : ")
    cuoi_ky = float(input())


    #Tính điểm trung bình
    trungbinh = (kiem_tra + giua_ky + cuoi_ky) / 3

    return trungbinh


def in_ket_qua(diem):
    """Hàm in kết quả lên màn hình"""
    print("Điểm trung bình là: ", trungbinh)
    if (diem < 5):
        print("F");
    elif (diem >= 5 and diem < 7):
        print("C")
    elif (diem >= 7 and diem < 9):
        print("B")
    elif (diem >= 9):
        print("A")
def cuoc_goi():
    a = int(input("nhap a:"))
    t = 25000
    if (a <= 50):
        t += a*600
    elif (a <= 200):
        t += 50*600 + (a-50)*400
    else:
        t += 50*600 + 150*400 + (a-200)*200
    print("Tong tien: ", t)

def tong():
    n = int(input("Nhap vao n "))
    summ = 0
    for i in range(n+1):
        print(i)
        summ += i
    print("Tong la: ",summ)

def tong2():
    n = int(input("Nhap vao n "))
    summ = 0
    for i in range (n+1):
        print(i)
        summ += 1/(2*i+1)
    print("Tong la ",summ)

def check(n):
    #0 là không phải SNT, 1 là SNT
    if n < 2:
        return False
    if n == 2:
        return True
    else:
        for i in range(2,n):
            if n % i == 0:
                return False
        return True
        
if __name__ == "__main__":
    rem = 0
    running = 1
    while (running == 1):

        print("\nnhap so 1 de Giải phương trình bậc 2")
        print("nhap so 2 Viết chương trình xếp hạng học lực của học sinh dựa trên các điểm bài kiểm tra, điểm thi giữa kỳ, điểm thi cuối kỳ")
        print("nhap so 3 de tinh tien cuoc goi")
        print("nhap so 4 de nhap vao n de tinh tong 1 + 2 + 3 + … + n ")
        print("nhap so 5 de tinh  1 + 1/3 + 1/5 + … + 1/(2n+1)")
        print("nhap so 6 Nhập số nguyên dương n từ bàn phím tính tổng lẻ tổng chẵn và chính phương ")
        print("nhap so 7 Nhập n, vẽ hình tam giác")
        rem = int(input("nhap: "))

        if rem == 1 :
            a = float(input("Nhập hệ số bậc 2, a = "));
            b = float(input("Nhập hệ số bậc 1, b = "));
            c = float(input("Nhập hằng số tự do, c = "));

            giaiPTBac2(a, b, c)

        if rem == 2 :
            trungbinh = nhap_diem()
            in_ket_qua(trungbinh)

        if rem == 3 :
            cuoc_goi()

        if rem == 4 :
            tong()

        if rem == 5 :
            tong2()

        if rem == 6 :
            n = int(input("Nhap so n "))
            sumodd = 0
            sumprime = 0
            sumsquare = 0
            for i in range(1,n+1,2):
                sumodd += i
            for i in range(1,n+1):
                if (check(i) == True):
                    sumprime += i
            for i in range (1,n+1):
                if (math.sqrt(i)).is_integer():
                    sumsquare += i
            print("Tong le: ", sumodd)
            print("Tong nguyen to: ", sumprime)
            print("Tong chinh phuong: ",sumsquare)

            check(n)

        if rem == 7 :
            n = int(input("Nhap n "))
            for i in range(1,n+1):
                for j in range(1,n+2-i):
                    print("*", end='')
                print("")
            print("")
            for i in range(1,n+1):
                if (i == 1):
                    for j in range(1,n+1-i):
                        print(" ", end='')
                    print("*", end='')
                    for j in range(1,n+1-i):
                        print(" ", end='')
                    print("")
                elif (i == n):
                    for j in range(2*n-1):
                        print("*", end='')
                else:
                    for j in range(1,n+1-i):
                        print(" ", end='')
                    print("*", end='')
                    for j in range(1,2*i-2):
                        print(" ", end='')
                    print("*", end='')
                    for j in range(1,n+1-i):
                        print(" ", end='')
                    print("")
            print("")

        elif rem == 0 :
            running = 0