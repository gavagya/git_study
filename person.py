class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
    	return self.name.split()[-1]
    def giveRaise(self, percent):
    	self.pay = int(self.pay*(1 + percent))
    def __str__(self):
    	return '[Person: {}, {}, {}]'.format(self.job, self.name, self.pay)

class Manager (Person):
	def __init__(self, name, pay):
		Person.__init__(self, name, 'mng', pay)
	def giveRaise(self,percent,bonus = .10):
		Person.giveRaise(self, percent + bonus)



if __name__ == '__main__':
	bob = Person('bob smith')
	sue = Person('Sue Jones', job='dev', pay=10000)
	tom = Manager('Tom Jones', pay = 20000)

	# print(bob.name,'\n',sue.name, end='')
	# print (bob.name.split()[-1])
	# sue.pay *= 1.10
	# print(sue.pay)

	# print(bob.lastName())
	sue.giveRaise(0.1)
	# print (sue.pay)
	print(sue)
	print(bob)


	tom.giveRaise(.10)
	print(tom.lastName())
	print(tom)