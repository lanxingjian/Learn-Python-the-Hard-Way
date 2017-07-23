print "Type the filename again:" # print
file_again = raw_input(">") # use raw_input() to get the data inputed by users,and let it equal to file_again

txt_again = open(file_again) # return the file object of "file_again",let it be txt_again

print txt_again.read() # txt_again.read() return the whole file ,and print it 

txt_again.close()