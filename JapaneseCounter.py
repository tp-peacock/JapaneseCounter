import sys

def readnumber():
	number = raw_input("Please enter a number: ")
	while type(number)!=int:
		if number.isdigit():
			return number
		else:
			number = raw_input("Error! Please enter an integer number: ")

def numsplit():
	number = readnumber()
	if len(number) == 1:
		print onetoten(number)
	if len(number) == 2:
		print type(number[0])
		print onetoten(number[0]),"-",onetoten(number[1])
	
def onetoten(n):
	str(n)
	numbers = { "1": "ichi",
	 			"2": "ni",
	 			"3": "san",
	 			"4": "yon", 
	 			"5": "go", 
	 			"6": "roku", 
	 			"7": "nana", 
	 			"8": "hachi", 
	 			"9": "kyuu", 
	 			"10": "juu"}
	return numbers[n]

numsplit()