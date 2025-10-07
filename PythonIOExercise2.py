#BYRON BAGHURST
#111
'''
print("NUM 111")

io = open("Books.csv", "w")

io.write(",Book, Author, Year Released")
io.write("\n")
io.write("0, To kill a mockingbird, Harper Lee, 1960")
io.write("\n")
io.write("1, A Brief History of Time, Stephen Hawking, 1988")
io.write("\n")
io.write("2, The Great Gatsby, F. Scott Fitzgerald, 1922")
io.write("\n")
io.write("3, The Man Who Mistook His Wife For A Hat, Oliver Sacks, 1985")
io.write("\n")
io.write("4, Pride and Prejudice, Jane Austen, 1813")
io.close()

#112
print("NUM 112")

userAddBook = input("Add a book name to the list: ")
userAddBookName = input("Add the author to the list: ")
userAddBookYear = input("Add the year to the list: ")
io = open("Books.csv", "a")
io.write("\n")
io.write(f"5,{userAddBook}, {userAddBookName}, {userAddBookYear}")
io.write("\n")
io.close()
io= open("Books.csv", "r")
for line in io:
    print(line)
io.close()

#113
print("NUM 113")

numTimes = int(input("How many more records do you want to add?: "))
num = 4
for i in range(numTimes):
    num += 1
    userAddBook = input("Add a book name to the list: ")
    userAddBookName = input("Add the author to the list: ")
    userAddBookYear = input("Add the year to the list: ")
    io = open("Books.csv", "a")
    io.write("\n")
    io.write(f"{num},{userAddBook}, {userAddBookName}, {userAddBookYear}")
    io.close()
    io= open("Books.csv", "r")
    for line in io:
        print(line)
    io.close()
'''
#114
print("NUM 114")

startYears = int(input("Enter a starting year: "))
endYears = int(input("Enter a ending year: "))
    
io= open("Books.csv", "r")
for line in io:
    for yearStart in range(startYears, endYears +1):
            
        if str(yearStart) in line:
            
            print(line)
            
    io.close()

            
        
