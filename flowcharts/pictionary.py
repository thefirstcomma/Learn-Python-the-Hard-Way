def guess():
	print "Did They Guess It?"
	print "Yes/No"
	input = raw_input('> ')
	
	if input == 'Yes' or input == 'yes':
		print "You Win."
	elif input == 'No' or input == 'no':
		print "Point Repeatedly to the Same Picture."
		guess()
	else:
		not_input()
	
def not_input():
	print "Not an option."
	
	
def start():
	print "How People Really Play Pictionary.\n"
	print "Draw A Picture"
	guess()
	
start()