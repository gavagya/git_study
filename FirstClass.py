class FirstClass:
	def __init__(self,name):
		self.name = name
	def setdata(self,value):
		self.data = value
		
	def display(self):
		print(" vaule of {} =".format(self.name), self.data)


x = FirstClass('first')
y = FirstClass('second')

x.setdata("GUrgen")
y.setdata(3.14)

x.display()
y.display()

# x.anotherspam = 'sam'
# print(x.anotherspam)

# print (y.anotherspam)

class SecondClass(FirstClass):
	def __init__(self):
		pass
	def display(self):
		print('Currnet value = {}'.format(self.data))

b = SecondClass()
b.setdata(313)
b.display()

# new comment lane
# new comment lane secind time