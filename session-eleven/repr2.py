class ClassB(object):
	def __init__(self, a=None):
		self.a = a

	def __repr__(self):
		return '%s(a=a)' % (self.__class__)
 
if __name__ == "__main__":
	a = ClassA()
	b = ClassB(a=a)
	a.b = b
	repr(a)
	repr(b)
