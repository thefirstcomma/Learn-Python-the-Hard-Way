class Parent(object):
	
	def implicit(self):
		print "PARENT implicit()"
	
class Child(Parent):
	pass


Parent().implicit()
Child().implicit()