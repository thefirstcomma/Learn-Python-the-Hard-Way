def notinput():
	print "Not an option."


def start():
	print "Lamp doesn't work"

	print "Lamp plugged in?"
	print "(yes) or (no)"

	input = raw_input('> ')

	if input == 'no':
		print "Plug in Lamp"

	elif input == 'yes':
		print "Is Bulb burned out?"
		print "(yes) or (no)"
	
		input2 = raw_input('> ')
		if input2 == 'yes':
			print "Replace bulb"
		elif input2 == 'no':
			print "Repair lamb"
		else:
			notinput()

	else:
		notinput()

start()
