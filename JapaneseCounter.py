import sys

def splash():
	print "------------------------------------------------"
	print "--------------- Japanese Counter ---------------"
	print "------------------------------------------------"
	print "      Enter an integer digit to translate       "
	print "      into Japanese, or enter 'Q' to quit.      "
	print "------------------------------------------------"


def readnumber():
	if len(sys.argv) == 2:
		return sys.argv[1]
	splash()
	number = raw_input("Please enter a number: ")
	while type(number)!=int:
		if number in ['q','Q']:
			print "Quitting..."
			return 0
		elif number.isdigit():
			return number
		else:
			number = raw_input("Error! Please enter an integer number: ")

def numsplit():
	number = readnumber()
	if number == 0: return 0
	jnumber = ""
	while len(number) > 0:			
		if len(number) == 1:
			jnumber += singledigits(number)
			number = number[1:]
			
		if len(number) == 2:
			jnumber += tens(number[0])
			number = number[1:]
			
		if len(number) == 3:
		 	jnumber += hundreds(number[0])
		 	number = number[1:]
		 	
		# else:
		# 	number = ""
		# 	return "Too large a number to process!"
	print jnumber
	return jnumber
	
def singledigits(n):
	numbers = { "0":"",
				"1": "ichi",
	 			"2": "ni",
	 			"3": "san",
	 			"4": "yon", 
	 			"5": "go", 
	 			"6": "roku", 
	 			"7": "nana", 
	 			"8": "hachi", 
	 			"9": "kyuu"}
	return(" "+numbers[n])

def tens(n):	
	numbers = { "0":"",
				"1": "juu",
	 			"2": "ni",
	 			"3": "san",
	 			"4": "yon", 
	 			"5": "go", 
	 			"6": "roku", 
	 			"7": "nana", 
	 			"8": "hachi", 
	 			"9": "kyuu"}
	if n == "0": return("")
	if n == "1": return(" "+numbers[n])
	else: return(" "+numbers[n]+"-"+numbers["1"])
	
def hundreds(n):
	numbers = { "0":"",
				"1": "yaku",
	 			"2": "nih",
	 			"3": "sanh",
	 			"4": "yonh", 
	 			"5": "goh", 
	 			"6": "ropp", 
	 			"7": "nanah", 
	 			"8": "happ", 
	 			"9": "kyuuh"}
	if n == "0": return("")
	if n == "1": return("h"+numbers[n])
	else: return(numbers[n]+numbers["1"])

def thousands(n):
	return 0

numsplit()





