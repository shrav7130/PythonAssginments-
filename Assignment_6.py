#Shravan Surve

def ds(roll_no, name):
    my_list = [roll_no, name]
    my_tuple = (roll_no, name)
    my_set = {roll_no, name}
    my_dict = {'Roll No': roll_no, 'Name': name}

   
    print("Initial data structures:")
    print("List:", my_list)
    print("Tuple:", my_tuple)
    print("Set:", my_set)
    print("Dictionary:", my_dict)

    # Modify the values during runtime
    new_roll_no = input("Enter new roll number: ")
    new_name = input("Enter new name: ")

    my_list[0] = new_roll_no
    my_list[1] = new_name

  
    my_tuple = (new_roll_no, new_name)

    my_set.remove(roll_no)
    my_set.add(new_roll_no)
    my_set.remove(name)
    my_set.add(new_name)

    my_dict['Roll No'] = new_roll_no
    my_dict['Name'] = new_name

    print("Modified data structures:")
    print("List:", my_list)
    print("Tuple:", my_tuple)
    print("Set:", my_set)
    print("Dictionary:", my_dict)

    # Delete the data structures
    del my_list
    del my_tuple
    del my_set
    del my_dict

    print("Data structures deleted.")


# testing the function
roll_no = input("Enter roll number: ")
name = input("Enter name: ")
ds(roll_no, name)