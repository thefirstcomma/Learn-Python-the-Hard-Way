numbers = []


def while_loop(end):
	i = 0

	while i < end:
		print "The top i is: %d" % i
		numbers.append(i)
	
		i += 3
		print "Number's now: ", numbers
		print "At the bottom i is: %d" % i


	print "\nThe numbers: "

	for num in numbers:
		print num

while_loop(8)

del numbers[:]

print "Now For Loops"
for start in range(0, 8, 3):
	numbers.append(start)
	
for num in numbers:
	print num