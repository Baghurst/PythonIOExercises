fin = open("bob.txt", "w")
fin.write("Hello bob")
fin.write("\n")
fin.write("Today is a new day")
fin.write("\n")
fin.close()

fin= open("bob.txt", "r")
for line in fin:
    print(line)
fin.close()