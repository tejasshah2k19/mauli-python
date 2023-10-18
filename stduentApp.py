students = [] 
courses = [] 

class Stduent:
    def __init__(self):
        self.id = 0 
        self.name = ""
        self.userName =""
        self.password = ""

    def signup(self):
        self.id = input("\nEnter Id")
        self.name = input("Enter Name")
        self.userName = input("Enter UserName")
        self.password = input("Enter Password")

    def login(self,userName,password):
        return userName == self.userName and password == self.password 
    
class Course: 
    def __init__(self):
        self.id = 0 
        self.name = ""
        self.capacity = 0 
        self.cstudent = []
    
    def addCourse(self):
        self.id = input("Enter CourseId")
        self.name = input("Enter course Name ")
        self.capacity = int(input("Enter Total Capacity"))
        self.cstudent = []
    
    def printData(self):
        print("\nId ",self.id)
        print("\nCourseName ",self.name)
        print("\nCapacity ",self.capacity)
        print("\nEnrollStudent : ")
        for s in self.cstudent :
            print(s.name)


d1 = Stduent()
d1.id = "1" 
d1.name = "x"
d1.userName = "x"
d1.password = "x"
students.append(d1)

d2 = Stduent()
d2.id = "2" 
d2.name = "y"
d2.userName = "y"
d2.password = "y"
students.append(d2)

d3 = Stduent()
d3.id = "3" 
d3.name = "z"
d3.userName = "z"
d3.password = "z"
students.append(d3)

c1 = Course()
c1.id= "1"
c1.name = "C"
c1.capacity = 2 

c2 = Course()
c2.id= "2"
c2.name = "C++"
c2.capacity = 2 

courses.append(c1)
courses.append(c2)





while True:
    print("\n0 For Exit\n1 For Signup\n2 For Login\n3 For AddCourse\n4List Courses\nEnter choice")
    choice = int(input())

    if choice == 0:
        exit(0)
    elif choice == 1:
        s = Stduent()
        s.signup()
        students.append(s) 
    elif choice ==  2 :
        userName = input("Enter userName ")
        password = input("Enter Password")

        flag = False 
        for s in students : 
            if s.login(userName,password) == True: 
                flag = True 
                print("\nWelcome To Canvas")
                print("\n1 For EnrollCourse\n2 For Logout\nEnter Choice")
                choice2 = int(input())

                if choice2 == 1 : 
                    for c in courses: 
                        print(c.id," ",c.name) 
                    print("\nPlease Enter Course Id for Enrollment")
                    courseId = input() 

                    for c in courses: 
                        if c.id == courseId:
                            if len(c.cstudent) == c.capacity:
                                print("\nSorry Course Full")

                            else:
                                print("\nEnrollment done")
                                c.cstudent.append(s)
                            
                                
                break 
        if flag == False:
            print("Invalid Credentials PTA!!")    

    elif choice == 3:
        c = Course()
        c.addCourse()
        courses.append(c)

    elif choice == 4:
        for c in courses:
            c.printData()