'''
Troy Alcala
November 5, 2018
CIS 245
Assignment 10.1
'''

import os #import the OS library

filePath = input('What file path would you like to use? ')
fileName = input('What file name would you like to use? ' )
trueFileName = fileName + '.txt'

completePath = filePath + '/' + trueFileName


if os.path.isdir(filePath): #check if file path exists
	print('Directory Exists')
else:
	os.mkdir(filePath)	#create directory if it does not exist
	print('Directory created')

if os.path.isfile(completePath):	#check if file exists
	print('File Exists')
else:
	print ("File doesn't exist")
  
if os.path.exists(completePath): #check if complete path exists
	print('Complete path exists', completePath)
else:
	print('Path ' + filePath + ' exists, file will be created under chosen name.') #if complete path does not exist, inform user file will be created

with open(completePath, 'a') as fileHandle: #open file for appending to avoid over writing
	fileHandle.write ('**New Entry**\n')
	fileHandle.write (input('What is your full name? '))
	fileHandle.write ('\n')			
	fileHandle.write (input('What is your address? '))				#write data to file
	fileHandle.write ('\n')	
	fileHandle.write (input('What is your phone number? ')) 
	fileHandle.write ('\n')	

readEntry = input('Would you like to read the contents of the file?\n1Yes\n2No\n ') #ask user if they would like to review file

if readEntry is '1':
	with open(completePath, 'r') as fileHandle: #open same file for reading
		data = fileHandle.read() #read data from the file
		print(data)
else:
	print('File can be viewed at ' + completePath) #give user filepath to view file
	
	
'''
I attempted to use this syntax but it would always go under if and never the else 
statement, looking it up it seems to be correct but I'm not sure, I am having 
the same issues with my final as well.

if readEntry == 'Y' or 'YES':
	with open(completePath, 'r') as fileHandle: #open same file for reading
		data = fileHandle.read() #read data from the file
		print(data)
else:
	print('File can be viewed at ' + completePath)
'''
