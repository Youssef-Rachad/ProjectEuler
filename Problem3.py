def largestFactor(num):
	largestFactor = 0
	currentNum = num #newnumm
	counter = 2

	while(counter**2 <= num):
		#true  is 1
		#false is 0
		control = (int)(currentNum%counter==0)
		#print("control is:" + str(control))
		#if not a divisor then control = 0
		currentNum = (control) * (currentNum / counter) + (1-control) * currentNum
		#print("currentNum is: " + str(currentNum))
		largestFactor = counter * (control) + largestFactor*(1-control)
		#print("largestFactor is:" + str(largestFactor))
		counter = counter + (1-control)
		
	largestFactor = largestFactor * (1-(int)(currentNum>largestFactor)) + currentNum * (int)(currentNum>largestFactor)
	#print("largestFactor is:" + str(largestFactor))

	print(largestFactor)

largestFactor(600851475143)
