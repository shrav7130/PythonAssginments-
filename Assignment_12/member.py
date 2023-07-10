

def add_member():
    name = input("Enter the name of the member: ")
    member_id = input("Enter the ID of the member: ")
    f=open("members.txt","a")
    f.write(f"{name},{member_id}")
    print("Member added successfully!")