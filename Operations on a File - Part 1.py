# Read Operations Part 1
#open file and read its contents
file = open('Codingal.txt','r')
print(file.read())
file.close()

#open file and read its beginning 8 characters
file = open('Codingal.txt','r')
print("\n Read in parts \n")
print(file.read(8))
file.close()

#append your name and age in the file
file = open('Codingal.txt','a')
file.write(" Hi! I am Penguin and I am 1 yr old.")
file.close()
# --------------------------------------------------------------
# Read Operations Part 2
#read first line of file
file = open('Codingal.txt','r')
print("Reading first line...")
print(file.readline())
file.close()

#read first three lines of file
file = open('Codingal.txt','r')
print("Reading multiple lines...")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

#looping through all the lines of the file
file = open('Codingal.txt','r')
print("Looping through the lines...")
for line in file:
  print(line)
file.close()
# ----------------------------------------------------------------
# Remove Lines
# Program to remove lines starting with any prefix

file1 = open('Codingal.txt',
			'r')
file2 = open('CodingalUpdated.txt',
			'w')

# reading each line from original
# text file
for line in file1.readlines():
	
	# reading all lines that do not
	# begin with "Coding"
	if not (line.startswith('Coding')):
		
		# printing those lines
		print(line)
		
		# storing only those lines that
		# do not begin with "Coding"
		file2.write(line)

# close and save the files
file2.close()
file1.close()
# -----------------------------------------------------------------
# Odd Lines
# Program to copy odd lines of one file to another
# open file in read mode
fn = open('Codingal.txt', 'r')

# open other file in write mode
fn1 = open('CodingalUpdated.txt', 'w')

# read the content of the file line by line
cont = fn.readlines()
type(cont)
for i in range(1, len(cont)+1):
	if(i % 2 != 0):
		fn1.write(cont[i-1])
	else:
		pass

# close the file
fn1.close()

# open file in read mode
fn1 = open('CodingalUpdated.txt', 'r')

# read the content of the file
cont1 = fn1.read()

# print the content of the file
print(cont1)

# close all files
fn.close()
fn1.close()
# ---------------------------------------------------------
# File Handling - Operations Part 1
#open file and read its contents
file = open('Sample_File.txt','r')
print(file.read())
file.close()

#open file and read its beginning 8 characters
file = open('Sample_File.txt','r')
print("\n Read in parts \n")
print(file.read(8))
file.close()

#read first line of file
file = open('Sample_File.txt','r')
print("\n Reading first line...")
print(file.readline())
file.close()

#read first three lines of file
file = open('Sample_File.txt','r')
print("\n Reading multiple lines...")
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

#looping through all the lines of the file
file = open('Sample_File.txt','r')
print("\n Looping through the lines...")
for line in file:
  print(line)
file.close()


