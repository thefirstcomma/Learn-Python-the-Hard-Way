import sys


# function countchars 
def countchars(filename):
	count = {}
	
	with open(filename) as info:
		readfile = info.read()
		for char in readfile.upper():
			count[char] = count.get(char, 0) + 1
	
	return count


# tests which version of python to appropriately gather input for filename
# if imported this is ignored, however '__main__' is your current home file/directory
# so since we have this file and it isn't imported __name__ = __main__
if __name__ == '__main__':
	if sys.version_info.major >= 3:
		input_func = input
	else:
		input_func = raw_input
	
	inputFile = input_func("File Name: ")
	print (countchars(inputFile))