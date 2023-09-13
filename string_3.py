print("Enter email")


email = input() #tejas@gmail.com  @gmail.com t@g.com 

#XX@XX.XX

emailIndex = -1; 
dotIntext = -1; 
count =0 
if len(email) >= 8:
    for i in range(0,len(email)):#0 1 2 3 4 5 6 7    
        if email[i] == '@':
            emailIndex = i 
            break

    for i in range(0,len(email)):
        if email[i] == '.':
            dotIntext = i
            break 
    
    for i in range(0,len(email)):
        if email[i] == '@':
            count = count + 1 

    if emailIndex >= 2 and dotIntext >= emailIndex+3 and count == 1:
        print("Valid")
    else:
        print("InValid")
else:
    print("InValid")