import math
#function used for filtering out
def func(x):
	if not (x%2 and math.floor(math.sqrt(x))**2==x):
		return x
	else:
		return -1
#main method
num=[i for i in range(1,31)]
#filtering out by map method
print("Using Map:",end=" ")
by_map=list(map(func,num))
for item in by_map:
	if item!=-1:
		print(item,end=" ")
print()
#filtering out by filter method
print("Using Filter:",end=" ")
print(list(filter(func,num)))
