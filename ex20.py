from sys import argv   # 

script, input_file=argv  #

def print_all(f):
    print f.read()       # 定义函数，函数功能打印出文件读取的所有内容
	
def rewind(f):             # 定义函数，函数的功能是重置文件读取从文件头开始
    f.seek(0)
	
def print_a_line(line_count, f):
    print line_count, f.readline()     # 定义一个函数，功能是输出行数，并且输出文件读取的一行内容
	
current_file = open(input_file)   # 打开文件

print "First let's print the whole file:\n"

print_all(current_file)       # 打印输出current_file 这个文件的所有内容

print "Now let's rewind, kind of like a tape."   

rewind(current_file)     # 调用函数，重置刚才的光标（刚才已经读取完文件的所有内容，光标应该在文件末尾

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)  

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1 
print_a_line(current_line, current_file)