#import module argv for command line input
from sys import argv

#assign variables from command line input
script, filename = argv

#assign var txt to function open(). opens filename variable from command-line input
txt = open(filename)

#simple print of the name of the textfile
print "Here's your file %r:" % filename
#uses function .read() with no parameters to go through the textfile
print txt.read()

#simple print statement asking for reassurance
print "Type the filename again:"
#2nd variable assigned for input using prompt '> ' looking for textfile
file_again = raw_input("> ")

#Another variable used to store open()'s return output of the file
txt_again = open(file_again)

#uses .read() to go through the file and output it to us
print txt_again.read()