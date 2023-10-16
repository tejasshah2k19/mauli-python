customers = []


while True:
    print("\n1 For Add Data\n2 For View All \n3 for Search Data\n4 Exit")
    print("Enter your choice")
    choice = int(input())

    if choice == 1:
        print("Enter Name and Mobile num")
        name = input()
        mobile = input()
        print("Total Amount and Category")
        amount = int(input())
        category  = input() 
        data = {"name":name,"mobile":mobile,"amount":amount,"category":category}
        customers.append(data)
    elif choice == 2:
        print(customers)
    elif choice == 3:
        pass 
    elif choice == 4:
        exit(0)
