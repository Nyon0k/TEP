from sys import stdin

def two_fractions(n):
	dict_frac = {}

	for i in range(1, n + 1):

		b = n + i
		a = (b*n)/i

		if a == int(a):
			dict_frac[int(a)] = b

	return dict_frac

for line in stdin:
	n = int(line)
	dict_frac = two_fractions(n)

	print(str(len(dict_frac)))

	for a, b in dict_frac.items():
		print("1/" + str(n) + " = 1/" + str(a) + " + 1/" + str(b))
