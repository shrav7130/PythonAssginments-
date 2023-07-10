

def add_book():
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    f=open("books.txt","a")
    f.write(f"{title},{author}")
    print("Book added successfully!")
