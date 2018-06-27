#imports the sys module
from sys import argv

#assigns two arguments
script, filename = argv

#opens the file
txt = open(filename)

#prints text and uses the filename
print "Heres your file %r:" % filename
#This prints the contents of the file
print txt.read()

#prints the quoted text
print "Type the filename again:"
#prompts for input
file_again = raw_input("> ")

#uses the raw_input to open a file
txt_again = open(file_again)

#prints the opened file
print txt_again.read()

close(txt)
close(txt_again)