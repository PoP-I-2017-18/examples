from timeit import Timer
from fibonacci import fib
from fibonacci_iterative import fib

print(fibonacci.fib(10))
#t1 = Timer("fib(10)","from fibonacci import fib")

for i in range(1,41):
	s = "fibonacci.fib(" + str(i) + ")"
	t1 = Timer(s,"from fibonacci import fib")
	time1 = t1.timeit(3)
	s = "fibonacci_iterative.fib(" + str(i) + ")"
	t2 = Timer(s,"from fibonacci_iterative import fib")
	time2 = t2.timeit(3)
	print("n=%2d, fib: %8.6f, fibi:  %7.6f, percent: %10.2f" % (i, time1, time2, time1/time2))