from sys import argv #import com-line input
from os.path import exists #import exists() method

script, copying_file, empty_file = argv #assign vars to argv

print "Copying from %s to %s" % (copying_file, empty_file) #print statement

indata = open(copying_file).read() #var = open first, then read or write

print "The input file is %d bytes long" % len(indata) #length of text in bytes

print "Does the output file exist? %r" % exists(empty_file) #exists() boolean
print "Ready, hit RETURN to continue, CTRL-C to abort." #print statement
raw_input('> ') # prompt asking

open(empty_file, 'w').write(indata) #copying file to file with .write() #will create a new .txt file if it DNE already

print "Alright, all done." #done