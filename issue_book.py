#Shravan Surve

def issue_book():
    book_title = input("Enter the title of the book: ")
    member_id = input("Enter the ID of the member: ")
    f=open("issue.txt","a")
    f.write(f"{book_title},{member_id}")
    print("Book issued successfully!")


    
