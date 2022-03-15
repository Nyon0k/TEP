from sys import stdin
from math import sqrt, pow, log

def prime_factors(n):
	dict_div = {}

	while n % 2 == 0:
		prime = 2
		dict_div[prime] = dict_div.get(prime, 0) + 1
		n /= 2
	
	while n % 3 == 0:
		prime = 3
		dict_div[prime] = dict_div.get(prime, 0) + 1
		n /= 3

	for i in range(5, int(sqrt(n)) + 1, 6):
		while n % i == 0:
			prime = i
			dict_div[prime] = dict_div.get(prime, 0) + 1
			n /= i

		while n % (i + 2) == 0:
			prime = i + 2
			dict_div[prime] = dict_div.get(prime, 0) + 1
			n /= prime

	if n > 4:
		prime = int(n)
		dict_div[prime] = dict_div.get(prime, 0) + 1

	return dict_div

for line in stdin:
	divides = True
	n, m = list(map(int, line.split()))

	if n >= m:
		print(str(m) + " divides " + str(n) + "!")
		continue

	if m == 0:
		print(str(m) + " divides " + str(n) + "!")
		continue

	if n == 0:
		if m != 1:
			print(str(m) + " does not divide " + str(n) + "!")
			continue
		else:
			print(str(m) + " divides " + str(n) + "!")
			continue

	div = prime_factors(m)

	for key, value in div.items():
		limit = int(log(n, key))
		beta = 0

		for exp in range(1, limit + 1):
			beta += n // pow(key, exp)
			
		if beta < value:
			divides = False
			break

	if divides:
		print(str(m) + " divides " + str(n) + "!")
	else:
		print(str(m) + " does not divide " + str(n) + "!")
