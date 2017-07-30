def cheese_and_crackers(cheese_count, boxes_of_crackers): # define the function cheese_and_crackers,and give it two parameters
    print "You have %d cheeses!" % cheese_count 
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket. \n"
	
	
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30) # use the function cheese_and_crackers with the arguments using the numbers directly.


print"OR, we can ust variables from our script:" # print
amount_of_cheese = 10  # define the variables, and let it assigned 10
amount_of_crackers = 50 # define the variables, and let it assigned 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers) # use the function with the arguments using variables 


print"We can even do math inside too:" # print 
cheese_and_crackers(10+20, 5+6)  # use the function cheese_and_crackers with the arguments doing math


print "And we can combine the two, variables and math:" # print
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) # use the function cheese_and_crackers with the arguments combined variables and math