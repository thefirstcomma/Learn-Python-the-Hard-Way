from sys import argv #import for command line input

script, input_file = argv #var setup for argv

def print_all(f):  #function print_all uses .read()
	print f.read()
	
def rewind(f):	#function uses.seek()
	f.seek(0)
	
def print_a_line(line_count, f): #function prints 1 line at a time
	print line_count, f.readline() #uses .readline() to print 1 whole line

#---------------------------------------------------------------

current_file = open(input_file) #open the inputted file

print "First let's print the whole file:\n"

print_all(current_file) #prints everything from inputfile

print "Now let's rewind kind of like a tape.\n"

rewind(current_file) #rewind(), since we read the cursor is essentially at the last character
#so rewind brings the cursor to the start again

print "Let's print three lines:\n"

print_a_line(1, current_file)
print_a_line(2, current_file)
print_a_line(3, current_file)