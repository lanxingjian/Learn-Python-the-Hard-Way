def apples_and_oranges(apples_count, boxes_of_oranges): 
    print "You have %d apples!" % apples_count 
    print "You have %d boxes of oranges!" % boxes_of_oranges
    print "Men, that's enough for a party!"
    print "Get a blanket. \n"
	
	
print "We can just give the function numbers directly:"
apples_and_oranges(20,30) 


print"OR, we can ust variables from our script:"
amount_of_apples = 10  
amount_of_oranges = 50 

apples_and_oranges(amount_of_apples, amount_of_oranges) 


print"We can even do math inside too:" 
apples_and_oranges(10+20, 5+6)  


print "And we can combine the two, variables and math:" 
apples_and_oranges(amount_of_apples + 100, amount_of_oranges + 1000) 

apples_and_oranges(20,amount_of_oranges)

apples_and_oranges(amount_of_apples,40)

apples_and_oranges(amount_of_apples * 30 + 10,amount_of_oranges / 5 - 10)

num_of_apples = raw_input("> input the numbers of apples:")
num_of_oranges = raw_input("> input the numbers of oranges:")
apples_and_oranges(int(num_of_apples),int(num_of_oranges))