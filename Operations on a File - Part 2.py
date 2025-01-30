# File Handling Operations Part 1
# write in file using with()function
with open('Codingal.txt', 'w') as file:
  file.write("Hi! I am Penguin and I am 1 yr old.")
file.close()

# split file into words
with open('Codingal.txt', 'r') as file:
  data = file.readlines()
  print("Words in this file are....")
  for line in data:
    word = line.split()
    print (word)
file.close()

# ---------------------------------------------------
# File Handling Operations Part 2
#create a new file
new_file = open('New_File.txt', 'x')
new_file.close()

#check if a file exists 
import os
print("Checking if my_file exists or not....")
if os.path.exists("my_file.txt"):
  os.remove("my_file.txt")
else:
  print("The file does not exist")

#create a new if it doesn't
my_file = open("my_file.txt", "w")
my_file.write("Hi! I am Penguin and I am 1 yr old.")
my_file.close()

#delete file named codingal
os.remove('Codingal.txt')

#delete the folder
os.rmdir('Folder')

# -------------------------------------------------------
# Duplicate Lines
# Program to eliminate repeated lines from a file

# creating the output file
outputFile = open('UpdatedFile.txt', "w")

# reading the input file
inputFile = open('Repeated.txt', "r")

# holds lines already seen
lines_seen_so_far = set()
print("Eliminating duplicate lines....")
# iterating each line in the file
for line in inputFile:

	# checking if line is unique
	if line not in lines_seen_so_far:

		# write unique lines in output file
		outputFile.write(line)

		# adds unique lines to lines_seen_so_far
		lines_seen_so_far.add(line)		

# closing the file
inputFile.close()
outputFile.close()
# ---------------------------------------------------------------
# File Merge
# Program to merge two files into a third file


# Reading data from file1
with open('Codingal.txt') as fp:
	data1 = fp.read()

# Reading data from file2
with open('sample_doc.txt') as fp:
	data2 = fp.read()
	
# Merging 2 files
# To add the data of file2
# from next line
data1 += "\n"
data1 += data2
print("Merging two files....")
with open ('MergedFile.txt', 'w') as fp:
	fp.write(data1)
# --------------------------------------------------------------------------
# File Handling - Operations Part 2
# write in file using with()function
with open('Sample_File', 'w') as file:
  file.write("Hi! I am Penguin and I am 1 yr old.")
file.close()

# split file into words
with open('Sample_File.txt', 'r') as file:
  data = file.readlines()
  print("Words in this file are....")
  for line in data:
    word = line.split()
    print (word)
file.close()

#check if a file exists 
import os
print("Checking if my_file exists or not....")
if os.path.exists("My_file.txt"):
  print("File exists")
else:
  print("The file does not exist")

#create a new if it doesn't
my_file = open("My_file.txt", "w")
my_file.write("Hi! I am Penguin. I am in class 8 studying in Pune.")
my_file.close()

#delete file named codingal
os.remove('Sample_doc.txt')
