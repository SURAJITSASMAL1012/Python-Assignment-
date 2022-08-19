n=int(input("enteer a range of numbers :"))


lst=list(range(n+1))
oddList=list(filter(lambda n: n%2!=0,lst))
squareOddList=list(map(lambda n : n*n,oddList))
print(squareOddList)