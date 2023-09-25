def task1(str):
    # a) word extract {split}
    # b) word first character capital 
    # c) word second to end character small 
    data = str.split(" ") #[Jony Jony yes Papa]
    isTitle = True  # i bel str is in title 

    for d in data: #jony   jony   yes   papa  
        # every first character == small or 2nd-last is in upper  
        if d[0].isupper() == False  or  d[1:len(d)].islower() == False:
            isTitle = False 
            break 
         

    if isTitle == True:
        print("valid")
    else:
        print("inValid")

#task1("jony jony yes papa")
#task1("JonY Jony Yes Papa")
#task1("Jony Jony Yes Papa")


def task2(str):
   dummy= ""
   str =  str.lower()
   for c in str:
    if c != 'a' and c != 'e' and  c != 'i' and c != 'o' and c != 'u':
        dummy = dummy + c
   print(dummy)


# task2("royal") #ryl 
# task2("ahmedabad")#hmdbd 


# str = input()
# dummy= ""
# str =  str.lower()
# for c in str:
#  if c != 'a' and c != 'e' and  c != 'i' and c != 'o' and c != 'u':
#     dummy = dummy + c
# print(dummy)



password = input()  #jony1234Pass 


for c in password:#j o n y 1 2 3 4 P a s s 
    if c.islower():
        pass 

        