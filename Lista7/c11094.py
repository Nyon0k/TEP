def dfs(x, y):
	global total
	if y < 0:
		y = m - 1
	if y >= m:
		y = 0
	if x < 0 or x >= n:
		return
	if used[x][y] != 0 or _map[x][y] != land:
		return

	used[x][y] = 1
	total += 1

	dfs(x+1, y)
	dfs(x, y+1)
	dfs(x-1, y)
	dfs(x, y-1)

while True:
	try:
		_map = []
		total = 0
		n, m = list(map(int, input().split()))
		used = [[0 for _ in range(m)] for _ in range(n)]

		for i in range(n):
			_map.append(list(input()))
		
		i, j = list(map(int, input().split()))
		land = _map[i][j]
		dfs(i, j)
		
		ans = 0

		for i in range(n):
			for j in range(m):
				total = 0
				dfs(i, j)
				if total > ans:
					ans = total

		print(ans)
		input()
	
	except EOFError:
		break
