
List_Student = []

class People:
    def __init__(self, ID, Name, Age):
        self.ID = ID
        self.Name = Name
        self.Age = Age
    
    def Set_ID(self, NewID):
        self.ID = NewID    
    def Set_Name(self, NewName):
        self.Name = NewName    
    def Set_Age(self, NewAge):
        self.Age = NewAge    
        
    def Get_ID(self):
        return self.ID  
    def Get_Name(self):
        return self.Name   
    def Get_Age(self):  
        return self.Age 
    
class Student(People):
    def __init__(self, ID, Name, Age, student_ID, diemTong):
        super().__init__(ID, Name, Age)
        self.studentID = student_ID
        self.diemTong = diemTong
       
    def Init(self, ID, Name, Age, student_ID, diemTong):
        self.Set_ID(ID)
        self.Set_Name(Name)
        self.Set_Age(Age)
        self.Set_studentID(student_ID)
        self.Set_diemTong(diemTong)
        
    
    def Set_studentID(self, NewstudentID):
        self.studentID = NewstudentID
    def Set_diemTong(self, NewdiemTong):
        self.diemTong = NewdiemTong
      
    def Get_studentID(self):
        return self.studentID
    def Total(self):
        return self.diemTong    
    
    def printInfor(self):
        print("****************")
        print("ID: " + self.ID)  
        print("Name: " + self.Name)   
        print("Age: " + str(self.Age))   
        print("StudentID: " + self.studentID)   
        print("DiemTong: " + str(self.diemTong))   

   
    
def Init():
    n = int(input("Nhập số lượng sinh viên: "))
    for i in range(n):
        ppT = Student(" ", " ", 0, " ", 0)
        print("Nhập ID sinh viên thứ " + str(i+1) + ": ")
        ppT.Set_ID(input())
        print("Nhập tên sinh viên thứ " + str(i+1) + ": ")
        ppT.Set_Name(input())
        print("Nhập tuổi sinh viên thứ " + str(i+1) + ": ")
        ppT.Set_Age(int(input()))
        print("Nhập mã số sinh viên thứ " + str(i+1) + ": ")
        ppT.Set_studentID(input())
        print("Nhập điểm tổng sinh viên thứ " + str(i+1) + ": ")
        ppT.Set_diemTong(float(input()))
        List_Student.append(ppT)

def ShowList():
    for i in List_Student:
        i.printInfor()
        
def Arrangement():
    for i in range(len(List_Student)):
        for j in range(i, len(List_Student)):
            if(int(List_Student[i].Total()) < int(List_Student[j].Total())):
                temp = Student(List_Student[i].Get_ID(), List_Student[i].Get_Name(), int(List_Student[i].Get_Age()), List_Student[i].Get_studentID(), int(List_Student[i].Total()))
                List_Student[i].Init(List_Student[j].Get_ID(), List_Student[j].Get_Name(), int(List_Student[j].Get_Age()), List_Student[j].Get_studentID(), int(List_Student[j].Total()))
                List_Student[j].Init(temp.Get_ID(), temp.Get_Name(), int(temp.Get_Age()), temp.Get_studentID(), int(temp.Total()))
          
if __name__ == "__main__":
    # Khởi tạo, nhập tên n sinh viên
    Init()
    # Sắp xếp theo thứ tự điểm tổng lớn đến nhỏ
    Arrangement()
    # In ra
    ShowList()

        
        
        
        
        
        
        
        
        
        
        