class ClassA(object):
	def __init__(self, b=None):
		self.b = b

	def __repr__(self):
		return '%s(%r)' % (self.__class__, self.b)


class ClassB(object):
	def __init__(self, a=None):
		self.a = a
	
	def __repr__(self):
		return "%s(%r)" % (self.__class__, self.a)

if __name__ == "__main__":
	a = ClassA()
	b = ClassB(a=a)
	a.b = b
	repr(b)