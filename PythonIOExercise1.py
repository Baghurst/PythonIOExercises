#105
io = open("Numbers.txt", "w")
io.write("1,")
io.write("2,")
io.write("3,")
io.write("4,")
io.write("5")
io.write("\n")
io.close()

#106
io2 = open("Names.txt", "w")
io2.write("Bob")
io2.write("\n")
io2.write("Steve")
io2.write("\n")
io2.write("Harry")
io2.write("\n")
io2.write("Voldemort")
io2.write("\n")
io2.write("Louis")
io2.write("\n")
io2.close()

#107
io2= open("Names.txt", "r")
for line in io2:
    print(line)
io2.close()

#108
userAdd = input("Add a name to the list: ")
io2 = open("Names.txt", "a")
io2.write(userAdd)
io2.close()
io2= open("Names.txt", "r")
for line in io2:
    print(line)
io2.close()

#109

print("Choose an option:")
print("1. Create a new file")
print("2. Display the file")
print("3. Add a new item to the file")

options = int(input("Enter your options (1-3): "))

#---OPTIONS---

if options == 1:
   io3 = open("Subjects.txt", "w")
   userSubject = input("Enter a school subject: ")
   io3.write(userSubject)
   io3.close()


elif options == 2:
    io3= open("Subjects.txt", "r")
    for line in io3:
        print(line)
    io3.close()
    


elif options == 3:
    userAddSubject = input("Add a new subject: ")
    io3 = open("Subjects.txt", "a")
    io3.write("\n")
    io3.write(userAddSubject)
    io3.write("\n")
    io3.close()
    io3= open("Subjects.txt", "r")
    for line in io3:
        print(line)
    io3.close()
  
#110
ioList = []
io2= open("Names.txt", "r")
for line in io2:
    ioList.append(line.strip())
io2.close()


nameDel = input("Enter one of those names: ")
print(ioList)

abc = ioList.index(nameDel)
print(abc)
ioList.remove(nameDel)
print(ioList)
