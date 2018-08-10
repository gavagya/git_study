from abc import ABCMeta, abstractmethod

class Super(metaclass = ABCMeta):
	def delegate(self):
		self.action()
	@abstractmethod
	def action():
		pass


# X = Super()

class Sub(Super):
	"""docstring for Sub"""
	def action(self): 
		print ('spam')

X = Sub()

X.delegate()