
def return_book():
    book_title = input("Enter the title of the book: ")
    member_id = input("Enter the ID of the member: ")
    
    lines = []
    f=open("issue.txt","r")
    lines = f.readlines()

    f=open("return_book.txt","w")
    for line in lines:
        if line.strip() != f"{book_title},{member_id}":
            f.write(line)
    
    print("Book returned successfully!")