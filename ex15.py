from sys import argv  # sys is a software package, this command means 

script, filename = argv # argument variables

txt = open(filename) # open() return a "file object",not comment itself.

print "Here's your file %r:" % filename # print 
print txt.read() # return the whole txt file

txt.close()