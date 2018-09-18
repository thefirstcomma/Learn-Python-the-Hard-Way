class Parent(object):
	
	def override(self):
		print "PARENT overide()"
	
class Child(Parent):
	
	def override(self):
		print "CHILD override()"


Parent().override()
Child().override()