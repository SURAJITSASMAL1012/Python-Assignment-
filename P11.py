def pythagoreanTriplets(limits) :
	c, m = 0, 2
    # Limiting c would limit all a, b and c
	while c < limits :
        #print("m=",m)
		for n in range(1, m) :
			a = m * m - n * n
			b = 2 * m * n
			c = m * m + n * n
 
            # if c is greater than limit then break it
			if c > limits :
				break
			print(a, b, c)
 
		m = m + 1
	return;

#main method
limit = int(input("Enter limit:"))
pythagoreanTriplets(limit)
