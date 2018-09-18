print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "So, you're %r old, %r tall, and %r heavy." % (age, height, weight)


print "What is your name?",
name = raw_input()
print "What college do you go to?",
college_name = raw_input()
print "Do you like fish and chips?",
answer = raw_input()
print "Do you like programming?",
second_answer = raw_input()
print "What do you do for fun?",
fun = raw_input()

print """
Hi %r, You go to %r and %r you do(n't) like fish and chips,
and %r do(n't) like programming and you %r for fun
""" % (name, college_name, answer, second_answer, fun)