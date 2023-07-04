#Shravan Surve

from operations import StringOperations,My_str_exception
str=input("Enter string:")
obj=StringOperations(str)
try:
    n1=1
    while n1==1:
        print("You can perform following operations on string:")
        print("1)String length \n2)Reverse Sstring \n3)Count words in String \n4)String in Upper-case \n5)String in Lower-case \n6)Capitalized String \n7)Check if string is palindrome")
        num=int(input("Enter your choice :"))

        if num== 1:   
            print("String length:",obj.str_length())
        elif num==2:    
            print("Reversed String:",obj.str_reverse())
        elif num==3:    
            print("Words in a string:",obj.str_count())
        elif num==4:    
            print("String in Uppercase:",obj.str_upper())
        elif num==5:    
            print("String in Lowercase:",obj.str_lower())
        elif num==6:   
            print("Capitalized String:",obj.str_capitalize())
        elif num==7:    
            print("Is entered string palindrome: ",obj.is_str_palindrome())
        else:
            print("Invalid choice")
        n=input("If you want to continue press 1 \n otherwise press any key ")
        if n!="1":
            exit()
        n1=int(n)

except My_str_exception as e:
    print("String operation error: ",e)
