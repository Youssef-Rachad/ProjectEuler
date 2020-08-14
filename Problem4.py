def palindrome(num):
	palindrome=0
	while(num>0):
		palindrome = palindrome*10+(num%10)
		num= num//10
	return palindrome

def findbigboi():
	bigboi=0
	for x in range(100,999):
		for y in range(100,999):
			if(((x*y)==(palindrome(x*y))) and (palindrome(x*y)>bigboi)):
				bigboi = palindrome(x*y)
				#print(bigboi)
	return bigboi

print(findbigboi())
