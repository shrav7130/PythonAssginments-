# Shravan Surve

def update_file(r_no, name, class_name, file="data.txt"):
    try:
        #Writting data
        f=open(file,"a")
        f.writelines([r_no +"\n" ,name + "\n" ,class_name +"\n"])
        print("Data added successfully")
        #Reading data
        f=open(file,"r")
        data=f.readlines()
        for line in data:
            print(line)
       
    except IOError :
        print("Unable to open or write to the file")


update_file("24","Shravan","CO")
