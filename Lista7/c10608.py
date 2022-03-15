from collections import defaultdict

def indices_dict(lis):
	d = defaultdict(list)
	for i,(a,b) in enumerate(lis):
		d[a].append(i)
		d[b].append(i)
	return d

def disjoint_indices(lis):
	d = indices_dict(lis)
	sets = []
	while len(d):
		que = set(d.popitem()[1])
		ind = set()
		while len(que):
			ind |= que 
			que = set([y for i in que 
						 for x in lis[i] 
						 for y in d.pop(x, [])]) - ind
		sets += [ind]
	return sets

def disjoint_sets(lis):
	return [set([x for i in s for x in lis[i]]) for s in disjoint_indices(lis)]

def longest(l):
	if len(l) == 0:
		return 1

	list_len = [len(i) for i in l]
	return max(list_len)

cases = int(input())

for _ in range(cases):
	n, m = list(map(int, input().split()))
	group = []

	for _ in range(m):
		group.append(tuple(map(int, input().split())))

	print(str(longest(disjoint_sets(group))))
