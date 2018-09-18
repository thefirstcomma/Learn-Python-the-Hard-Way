from sys import exit

# print Dead for sake of un-repetition
def dead(why):
	print why
	print "You are Dead!"


# option 3 from start()
def insane():
	print "insane"
	
# option 1 from start()
def light_lighter():
	print """
	You light your lighter.
	The room barely visible, you first see just red.
	Then you notice blood everywhere.
	The smell suddenly unbearable.
	You see a variety of torn limbs in what appears to be an operating room.
	Footsteps are abruptly heard.
	Do you:
	
	(1) Get cover under the operating table?
		or
	(2) Run for the Exits!
	"""
	
	input = raw_input('> ')
	
	if input == '1':
		table_cover()
	elif input == '2':
		lighter_exit()
	else:
		not_option(input)
		light_lighter()

# option 2 for light_lighter()
def lighter_exit():
	print "You stumble and fall."
	print "Hearing the sudden movement. The Doors fling open."
	print "Out comes Shrek."
	print "Shrek roars and takes out his chainsaw."
	dead("Shrek sliced you into meaty parts.")

# Not a choice
def not_option(choice):
	print choice, "is not an option"

# beginning, or recursive. Surgery Room location.
def start():
	print """
	You're in a dark room.
	What do you do?\n
	(1) Light your lighter.
	(2) Stumble around until you find something?
	(3) Slowly go insane?
	"""
	
	input = raw_input('> ')
	
	if input == '1':
		light_lighter()
	elif input == '2':
		stumble()
	elif input == '3':
		insane()
	else:
		not_option(choice)
		print "\n"
		start()
		

# option 2 from start()
def stumble():
	print "stumble"


#option 1 for light_lighter()
def table_cover():
	print """
	You slowly crawl under the table and hear doors open!
	A slimy green ogre is brought to your attention.
	Shrek roars in confusion and searches for his obvious next dinner.
	
	The chainsaw is sprung alive and he approaches the table.
	"""
	dead("Sadly, he heard your whimpering and sliced you into 4's.")


start()