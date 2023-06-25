# This is a program for reading files and counting the number of lines in the file 
fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print(fname, 'is an invalid file name')
    quit()

for line in fhand:
    line = line.rstrip()
    count = fhand.read()
    line = count[ : 300]
    print('Total lines in this file: ',len(count))
    print(line.upper())
    

  
