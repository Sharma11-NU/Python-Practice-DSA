name = input(" what is your name : ")
age = int(input( " what is your age : "))

with open ("student.txt", "r+" ) as file :
    file.seek(0,2)
    file.write("\n" + "Name : " + name + "\n")
    file.write("Age : " + str(age))
    file.seek(0)
    content = file.read()
print(content)


