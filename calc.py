print("Enter two numbers")
a = int(input())
b = int(input())

print("Press 1 For Addition")
print("Press 2 For Subtraction")
print("Press 3 For Multiplication")
print("Enter your choice")

choice = int(input())

if choice == 1:
    ans = a + b
    print("addition = ",ans)

elif choice == 2:
    ans = a - b
    print("subtraction = ",ans)

elif choice == 3:
    ans  = a * b 
    print("multiplication = ",ans)

else:
    print("Invalid Choice!! PTA !!")


