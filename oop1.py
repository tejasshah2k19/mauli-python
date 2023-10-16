class Customer:
    # gorceryAmt , transportAmt , enterAmt 
    # name email password

    #constructor 
    def __init__(self):
        self.name = ""
        self.email = ""
        self.password = ""
        self.groceryAmt = 0
        self.transportAmt = 0
        self.entertainmentAmt = 0 

    def signup(self):
        print("Enter FirstName")
        self.name = input()
        print("Enter Email and Password")
        self.email = input()
        self.password = input()
        
    def printData(self):
        print("name : ",self.name)
        print("email : ",self.email)
        print("password : ",self.password)
        print("grocerAmt : ",self.groceryAmt)
        print("transportAmt : ",self.transportAmt)
        print("entertainmentAmt : ",self.entertainmentAmt)

    def addGrocery(self,amt):
        self.groceryAmt = self.groceryAmt + amt 
    
    def addEntertainment(self,amt):
        self.entertainmentAmt = self.entertainmentAmt + amt 
        
    def addTransport(self,amt):
        self.transportAmt = self.transportAmt + amt 
    
    def login(self,email,password):
        return self.email == email and self.password == password 
 



list = [] 

while True:
    print("1 For Signup\n2 For Login\n3 For Exit\n4 for Print all Customers\nEnter your choice")
    choice = int(input())

    if choice == 1:
        c = Customer() # create customer object {g e t name em pass}
        c.signup()
        list.append(c) # [c]
    elif choice == 2:
        print("Enter Email And Password")
        e =input()
        p = input()
        flag = False 
        for x in list:
            if  x.login(e,p) == True : 
                flag = True 
                while True:
                    print("\nWelcome To Expense Manager")

                    print("\n\t1 For Add Expense\n\t2 For View All Exp\n\t3 For Logout")
                    choice2 = int(input())

                    if choice2 == 1:
                        print("\n\t\t1 For Add Grocery Amt\n\t\t2 For Add Entertainment\n\t\t3 For Add Transport")
                        choice3 = int(input())

                        print("\nEnter Amount ")
                        amt = int(input())

                        if choice3 == 1:
                            x.addGrocery(amt)
                        elif choice3 == 2:
                            x.addEntertainment(amt)
                        elif choice3 == 3:
                            x.addTransport(amt)    
                    elif choice2 == 2:
                        x.printData()
                    elif choice2 == 3:
                        print("\n\tThank you For Using Our Service")
                        break #break current loop -> line num 62 

        if flag == False:
            print("Invalid Credentials")
    elif choice == 3:
        exit(0)
    elif choice == 4: 
        for x in list: 
            print(x.name)
