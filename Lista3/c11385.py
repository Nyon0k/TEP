def fibonacci(n):
	a = 1
	b = 2
	sum = 3
	count = 2
	dict_fibo = {1:0, 2:1}
	
	while(sum <= n):
		dict_fibo[sum] = count
		a = b
		b = sum
		sum = a + b
		count += 1
	return dict_fibo
    
n = int(input())
for i in range(n):
	input()
	fib_list = list(map(int, input().split()))
	texto = list(filter(lambda x: x.isupper(), input()))

	fib = fibonacci(2**31)
	res = [" "]*100
	cont = 0
	for j in fib_list:
		pos = fib[j]
		if pos < len(res):
			res[pos] = texto[cont]
			cont += 1
	print(''.join(res).rstrip())
