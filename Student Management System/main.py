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
        for i in range(ls.__len__()):
            if(ls[i].rollno == rn):
                return i
    
    def delete(self,rn):
        i = obj.search(rn)
        del ls[i]
    