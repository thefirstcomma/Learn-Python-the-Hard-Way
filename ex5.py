name = 'Zed A. Shaw'
age = 35 #not a lie
height = 74 #inches
weight = 180 #pounds
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %r." % name
print "He's %r inches tall." % height
print "He's %r pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %r eyes and %r hair." % (eyes, hair)
print "His teeth are usually %r depending on the coffee." % teeth

#this line is tricky and try to get it exactly right
print "If I add %d %d, and %d I get %d." % (age, height, weight, age + height + weight)