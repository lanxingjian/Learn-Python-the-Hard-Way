from sys import argv

script, first , second ,third,=argv



print "The script is called :",script
print "Your first variable is :",first
print "Your second variable is :" ,second
print "Your third variable is :\n",third

age = raw_input("How old are you?")
height = raw_input("How tall are you ?")
weight = raw_input("How much do you weigh ? ")

print "So, you're %r old\n\t ,%r tall\n\t and %r heavy\n\t." %(age , height,weight)
