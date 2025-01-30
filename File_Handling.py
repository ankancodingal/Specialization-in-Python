# File Handling Operations Part 1
# open file and store file object in a variable
file = open('Codingal.txt')

# read the contents of file
print(file.read())

# close the file
file.close()
# ---------------------------------------
# File Handling Operations Part 2
# open the file in read mode
file_read = open('Codingal.txt','r')
print("File in Read Mode -")
print(file_read.read())
file_read.close()

# open the file in write mode
file_write = open('Codingal.txt', 'w')
# write in the file 
file_write.write(" File in write mode ....")
file_write.write("Hi! I am Penguin. I am 1 yr. old ")
file_write.close()

# open the file in append mode
file_append = open('Codingal.txt', 'a')
# append in the file 
file_append.write("\n File in append mode ....")
file_append.write("Hi! I am Penguin. I am 1 yr. old")
file_append.close()
# ------------------------------------------------------
# Lines in File
# Program to count number of lines in this file
# Opening a file
file = open("Codingal.txt","r")
Counter = 0

# Reading from file
Content = file.read()
# splitting content into lines
# and storing them in a list
CoList = Content.split("\n")

for i in CoList:
	if i:
		Counter += 1
		
print("This is the number of lines in the file")
print(Counter)
# ---------------------------------------------------------
# Append Content
# Program to append contents of file in another file

# entering the file names
firstfile = input("Enter the name of first file ")
secondfile = input("Enter the name of second file ")

# opening both files in read only mode to read initial contents
f1 = open(firstfile, 'r')
f2 = open(secondfile, 'r')

# printing the contens of the file before appending
print('content of first file before appending -\n', f1.read())
print('content of second file before appending - \n', f2.read())

# closing the files
f1.close()
f2.close()

# opening first file in append mode and second file in read mode
f1 = open(firstfile, 'a+')
f2 = open(secondfile, 'r')

# appending the contents of the second file to the first file
f1.write(f2.read())

# relocating the cursor of the files at the beginning
f1.seek(0)
f2.seek(0)

# printing the contents of the files after appendng
print('content of first file after appending - \n', f1.read())
print('content of second file after appending - \n', f2.read())

# closing the files
f1.close()
f2.close()
# --------------------------------------------------------------------------
# File Handling - Access Modes
# open the file in read mode
file_read = open('Sample_File.txt','r')
print("File in Read Mode -")
print(file_read.read())
file_read.close()

# open the file in write mode
file_write = open('Sample_File.txt', 'w')
# write in the file 
file_write.write(" File in write mode ....")
file_write.write("Hi! I am Penguin. I am a class 8 student from Pune")
file_write.close()

# open the file in append mode
file_append = open('Sample_File.txt', 'a')
# append in the file 
file_append.write("\n File in append mode ....")
file_append.write("Hi! My favourite subject is Mathematics")
file_append.close()
