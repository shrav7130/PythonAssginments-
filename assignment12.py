#Shravan Surve

import book
import member
import issue_book
import returnbook

n1=1
while n1==1:
        print("This is library management system")
        print("1. Add a new book")
        print("2. Add a new member")
        print("3. Issue a book")
        print("4. Return a book")
        

        choice = input("Enter your choice: ")

        if choice == "1":
            book.add_book()
        elif choice == "2":
            member.add_member()
        elif choice == "3":
            issue_book.issue_book()
        elif choice == "4":
            returnbook.return_book()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
        n=input("If you want to continue press 1 \n otherwise press any key ")
        if n!="1":
            exit()
        n1=int(n)
