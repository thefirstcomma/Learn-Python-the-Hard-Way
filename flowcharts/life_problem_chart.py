def start():
	print "Do you have a problem in life"
	print "(y/n)"
	input = raw_input('> ')
	
	if input == 'y':
		print "Can you do something about it?"
		print "(y/n)"
		input2 = raw_input('> ')
		
		print "Then don't worry."
	
	elif input == 'n':
		print "Then don't worry."
	
	
	else:
		not_input()


def not_input():
	print "Not an input, doofus."
	

start()