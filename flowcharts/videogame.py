def adventure():
	a = "(1) Protagonist. Shirtless"
	b = "(2) Support. Fills diversity requirement."
	c = "(3) Villain. Demon/Monster. (OR russian)"
	
	print "Adventure Genre"
	print "(1) Protagonist. Shirtless"
	print "(2) Support. Fills diversity requirement."
	print "(3) Villain. Demon/Monster. (OR russian)"
	input = raw_input("> ")
	
	if input == '1':
		return a
	elif input == '2':
		return b
	elif input == '3':
		return c
	else:
		not_input()


def not_male():
	print """
	.
	.
	.
	.
	.
	
	"""
	
def not_input():
	print "Not an Input"

def rpg():
	a = "Protagonist. (1) American. User defined."
	b = "Protagonist. (2) Japanese. Japanese carries GIANT Sword"
	c = "Villain. (3) Demon/Monster"
	
	print "RPG"
	print "Protagonist. (1) American. User defined."
	print "Protagonist. (2) Japanese. Japanese carries GIANT Sword"
	print "Villain. (3) Demon/Monster"
	
	input = raw_input("> ")
	
	if input == '1':
		return a
	elif input == '2':
		return b
	elif input == '3':
		return c
	else:
		not_input()

def shooter():
	a = "Protagonist. White, Human, stoic, messianic."
	b = "Support. Aliens Cast Basically."
	c = "Villain. Russian, bulletproof."
	
	print "SHOOTER"
	print "(1) Protagonist. White, Human, stoic, messianic."
	print "(2) Support. Aliens Cast Basically."
	print "(3) Villain. Russian, bulletproof."
	
	print "What's your pick?"
	input = raw_input("> ")
	
	if input == '1':
		return a
	elif input == '2':
		return b
	elif input == '3':
		return c
	else:
		not_input()

def start():
	print "How Video Game Makers Design Characters."
	print "Gender??"
	print "(Female) or (Male)"
	gender = raw_input('> ')
	
	if gender == 'Female':
		not_male()
		not_male()
		not_male()
		print "BOOBS"
		
	elif gender == 'Male':
		shooter()
		rpg()
		adventure()
		
	else:
		not_input()


start()