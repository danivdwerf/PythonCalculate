import sys

class calculate():
	def __init__(self):
		self.startValue = sys.argv[1]
		self.start()

	def start(self):
		first = raw_input("Fill in first the first number: ")
		one = self.checkInput(first)

		second = raw_input("Now fill in the second number: ")
		two = self.checkInput(second);

		if self.startValue == "add":
			answer = self.add(one,two)
			print one," + ",two, " = ", answer
			sys.exit("I'm so done with you, bye")

		if self.startValue == "multiply":
			answer = self.multiply(one, two)
			print one, " * ", two, " = ", answer
			sys.exit("I'm so done with you, bye")
			

	def add(self,val1,val2):
		temp = (val1+val2)
		return temp

	def multiply(self,val1, val2):
		temp = (val1 * val2)
		return temp


	def checkInput(self,theInput):
		if "," in theInput:
			theInput = theInput.replace(",",".")
		try:
			temp = int(theInput)
			return temp
		except:
			try:
				temp = float(theInput)
				return temp
			except:
				print("Input was a string, only integers and floats are accepted")
				self.start()
var = calculate()