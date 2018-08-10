def classtree(cls, indent):
	print('.'*indent +cls.__name__)
	for supercls in cls.__bases__:
		classtree(supercls, indent+3)

def instancetree(inst):
	print('Tree of', inst.__class__.__name__, 'type object')
	classtree(inst.__class__, 3)
	print()


def selftest():
	class A: pass
	class B(A): pass
	class C(A): pass
	class D(B,C): pass
	class E: pass
	class F(D,E): pass

	a = B()
	print(type(a))
	instancetree(a)
	instancetree(F())

if __name__ == '__main__':
	selftest()