def evenFibo():
	fib1 = 1
	fib2 = 1
	result = 0
	summed = 0
	while(result < 4000000):
		summed += (1- (result%2)) * result

		result = fib1 + fib2
		fib2 = fib1
		fib1 = result
	print(summed)

evenFibo()
