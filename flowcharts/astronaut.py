def alien():
	print "Are You really just in it to meet the Aliens? (y/n)"
	alien = raw_input('> ')
						
	if alien == 'y':
		print "Seti Researcher, until all the funding is pulled out."
						
	elif alien == 'n':
		print "They won't live up to the hype huh."
		print "Sci-Fi Writer for you."


def not_input():
	print "Not an input"


def plane():
	print "Can you fly a plane?"
	fly = raw_input('> ')
		
	if fly == 'y':
		print "Dude, just be a pilot!\n"
		print "But if you hate space, then"
		print "Type 'No, I hate space' to keep looking."
		spacepilot = raw_input('> ')
			
		if spacepilot == 'No, I hate space':
			# function russian is used here
			russian()
				
		else:
			print "Dream job found"
			exit(0)
			
	elif fly == 'n':
		russian()
		
	else:
		not_input()
	
	
def russian():
	print "Do you speak russian? (y/n)"
	russian_speaker = raw_input('> ')
				
	if russian_speaker == 'y':
		print "Be an Astronaut, but hitch a ride with the Ruskies."
					
	elif russian_speaker == 'n':
		# function alien() is used within this function
		alien()
						
	else:
		not_input()
			

def star_wars():
	print "Does your favorite movie have 'Star' in the title? (y/n)"
		
	star = raw_input('> ')
		
	if star == 'n':
		print "GIVE UP THE DREAM!"
		print "You don't really love space anyways."
		exit(0)
		
	elif star == 'y':
		print "Can you withstand long hours staring at a computer screen?"
		print "(y/n)"
		screen = raw_input('> ')
			
		if screen == 'y':
			print "Duh, Obviously"
			# calls function alien()
			alien()
				
		elif screen == 'n':
			# calls function plane()
			plane()
			
		else: 
			not_input()


def start():
	print "What is the ideal space career for you?"
	print "Do you have a degree in science or enginnering? (y/n)"
	
	degree = raw_input("> ")
	
	if degree == 'y':
		plane()
	
	elif degree == 'n':
		star_wars()
			
	else:
		not_input()



start()