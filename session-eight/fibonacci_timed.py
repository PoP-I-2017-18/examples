from timeit import Timer

#t1 = Timer("fib(10)","from fibonacci import fib")

for i in range(1,41):
	s = "fib(" + str(i) + ")"
	t1 = Timer(s,"from fibonacci import fib")
	time1 = t1.timeit(3)
	t2 = Timer(s,"from fibonacci_iterative import fib")
	time2 = t2.timeit(3)
	t3 = Timer(s,"from fibonacci_memo import fib")
	time3 = t3.timeit(3)

	print("n=%2d, fib: %8.6f, fib iterative: %8.6f, percent: %10.2f, fib memo: %8.6f, percent (iterative vs memo): %10.2f" % (i, time1, time2, time1/time2, time3, time1/time3))