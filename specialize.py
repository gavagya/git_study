class Super():
	"""docstring for super"""
	def method(self):
		print('in Super.method')
	def delegate(self):
		self.action()

class Inheritor(Super):
	"""docstring for Inheritor"""
	pass


class Replacer(Super):
	def method(self):
		print('in Replacer.method')

class Extender(Super):
	def method(self):
		print('starting Extender.method')
		Super.method(self)
		print('ending Extender.method')


class Provider(Super):
	"""docstring for Provider"""
	def action(self):
		print('in Provider.action')

if __name__ == '__main__':
	for klass in (Inheritor, Replacer, Extender):
		print('\n' + klass.__name__ + '...')
		klass().method()

	# for klass in (Inheritor(), Replacer(), Extender()):
	# 	print('\n' + klass.__class__.__name__ + '...')
	# 	klass.method()
	print(klass.__name__)
	print(type(klass), '\n', type(klass()))
	# print ('\n Provider ...')
	klass = Provider()
	# klass.delegate()

