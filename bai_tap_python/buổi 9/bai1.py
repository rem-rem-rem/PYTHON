
class Employee:
    # def __init__(self, ID, Name, Salary):
    #     self.ID = ID
    #     self.Name = Name
    #     self.Salary = Salary
    Salary = 0
    def __init__(self):
        self.ID = "123456789"
        self.Name = "ABCDEFGH"
        self.Salary = 1000.0
        
    def init(self, ID, Name, Salary):
        self.Set_ID(ID)
        self.Set_Name(Name)
        self.Set_Salary(Salary)
    
    def Set_ID(self, NewID):
        self.ID = NewID    
    def Set_Name(self, NewName):
        self.Name = NewName    
    def Set_Salary(self, NewSalary):
        self.Salary = NewSalary    
        
    def Get_ID(self):
        return self.ID  
    def Get_Name(self):
        return self.Name   
    def Get_Salary(self):
        return self.Salary 
    
    def raiseSalary(self, amount):
        self.Salary = self.Salary + amount
        
    def ShowInfor(self):
        print(type(self.ID))
        print("ID: ", self.ID)
        print("Name: ", self.Name)
        print("Salary: ", str(self.Salary))



Employee_List = []         

def NewEmployee(Employee_t):
    Employee_List.append(Employee_t)

def ShowList():
    for i in Employee_List:
        print("#####################")
        i.ShowInfor()

def Arrangement():
    for i in range(len(Employee_List)):
        for j in range(i, len(Employee_List)):
            if(int(Employee_List[i].Salary) > int(Employee_List[j].Salary)):
                temp = Employee()
                temp.init(Employee_List[i].Get_ID(), Employee_List[i].Get_Name(), Employee_List[i].Get_Salary())
                Employee_List[i].init(Employee_List[j].Get_ID(), Employee_List[j].Get_Name(), int(Employee_List[j].Salary))
                Employee_List[j].init(temp.Get_ID(), temp.Get_Name(), temp.Get_Salary())
    

if __name__ == "__main__":
    # Tạo 3 Employee
    ppA = Employee()
    ppA.init("11200", "ABC", 1280)
    ppB = Employee()
    ppB.init("11201", "DEF", 500)
    ppC = Employee()
    ppC.init("11202", "GHI", 921)
    # Thêm 3 EMployee vào danh sách
    NewEmployee(ppA)
    NewEmployee(ppB)
    NewEmployee(ppC)
    # Sắp xếp
    Arrangement()
    # In ra.
    ShowList()






