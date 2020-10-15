#method1

def squaresum(n) : 

	
	sm = 0
	for i in range(1, n+1) : 
		sm = sm + (i * i) 
	
	return sm 


n = 6
print(squaresum(n))



#method2

def squaresum(n): 
	return (n * (n + 1) / 2) * (2 * n + 1) / 3


n = 6
print(squaresum(n))


 


