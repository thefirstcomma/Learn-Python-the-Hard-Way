class Parent(object):
	
	def altered(self):
		print "Parent altered()"
	
class Child(Parent):
	
	def altered(self):
		print "Child, before Parent altered()"
		super(Child, self).altered()
		print "Child, after Parent altered()"

Parent().altered()
Child().altered()