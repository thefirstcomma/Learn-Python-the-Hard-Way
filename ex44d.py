class Parent(object):
	
	def override(self):
		print "PARENT override()"
	
	def implicit(self):
		print "PARENT implicit()"
	
	def altered(self):
		print "PARENT altered()"

class Child(Parent):
	
	def override(self):
		print "CHILD override()"
	
	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		super(Child, self).altered()
		print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

# Parent override
dad.implicit()
# Parent override
son.implicit()

# parent override
dad.override()
# Child override
son.override()

# parent override
dad.altered()
# child before
# Parent Altered
# child after
son.altered()