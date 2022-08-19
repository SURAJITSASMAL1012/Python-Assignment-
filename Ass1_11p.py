import math
lst=[(i,j,k) for i in range(10) for j in range(10) for k in range(int(math.sqrt(2*11**2)))]
updatedlist=list(filter(lambda c:c[0]**2+c[1]**2==c[2]**2,lst))
print(updatedlist)