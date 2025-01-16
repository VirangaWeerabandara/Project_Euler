import time,math


start =time.time()

def sieve(n):
	is_prime = [True]*n
	is_prime[0] = False
	is_prime[1] = False

	#Using the sieve algorithm
	for i in range(2,int(math.sqrt(n)+1)):
		index = i*2
		while index < n:
			is_prime[index] = False
			index += i
	
	#List to store the prime numbers
	prime = []

	#adding prime to the list
	for i in range(n):
		if is_prime[i] == True:
			prime.append(i)
	return prime


print (sum(sieve(2000000)))


end_time = time.time()


print (end_time  - start)