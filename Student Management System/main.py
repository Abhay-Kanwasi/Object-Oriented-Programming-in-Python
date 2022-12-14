class Student:
    def __init__(self,name,rollno,m1,m2) -> None:
        self.name = name 
        self.rollno = rollno
        self.m1 = m1
        self.m2 = m2
    
    def accept(self,Name,Rollno,Marks1,Marks2):
        ob = Student(Name, Rollno, Marks1, Marks2)
        ls.append(ob)
    
    def display(self,ob):
        print("Name : ",ob.name)
        print("Rollno : ",ob.rollno)
        print("Marks1 : ",ob.m1)
        print("Marks2 : ",ob.m2)
    
    def search(self,rn):
        for i in range(len(ls)):
            if(ls[i].rollno == rn):
                return i

    
    def delete(self,rn):
        i = obj.search(rn)
        del ls[i]
    
    def update(self,rn,No):
        i = obj.search(rn)
        roll = No
        ls[i].rollno = roll

ls = []
obj = Student('',0,0,0)

print("\nOperation Used ")
print("\n1. Accept student details\n2. Display student details\n3. Search details of a student.\n4. Delete details of the student\n5. Update studnet details\n6. Exit")
while True:
    ch = int(input("Enter your choice : "))
    if(ch == 1):
        name = input("Enter the name : ")
        rollno = int(input("Enter the roll no. : "))
        marks1 = int(input("Enter your marks in first subject : "))
        marks2 = int(input("Enter your marks in secod subject : "))
        print("Saved")
        obj.accept(name,rollno,marks1,marks2)
    elif(ch == 2):
        print("\n")
        print("List of Students\n")
        for i in range(ls.__len__()):
            obj.display(ls[i])
    elif(ch==3):
        rn = int(input("Enter the roll no. : "))
        Student.search(rn)
        print("Student found")

    elif(ch == 4):
        obj.delete(2)
        print(ls.__len__())
        print("List after deletion")
        for i in range(ls.__len__()):
            obj.display(ls[i])
    elif(ch == 5):
        obj.update(3,2)
        print(ls.__len__())
        print("List after updation")
        for i in range(ls.__len__()):
            obj.display(ls[i])

    else:
        print("Thank You!")
    