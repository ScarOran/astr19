#write a python program that defines function
#f(x) that returns x**3+8. In the main function
#of the program, call f(x) with x = 9 and print
#the result. Use an if statement that executes
#if the result is larger tahn 27 and prints "YAY!"

#defining function f(x) to solve math problem
def f(x):
	return  x**3+8
	

#defining function main() that calls to and prints f(x)
def main():
	result = f(9)
	print(result)
	if result > 27:
		print('YAY!')
	else:
		''




#create statement that calls to"__main__"
if __name__=='__main__':
	main()

