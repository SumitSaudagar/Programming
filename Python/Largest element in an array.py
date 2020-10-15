
def largest(arr,n): 

	
	max = arr[0] 

	for i in range(1, n): 
		if arr[i] > max: 
			max = arr[i] 
	return max

arr = [7, 40, 21, 500, 107, 212] 
n = len(arr) 
Ans = largest(arr,n) 
print ("Largest in given array is",Ans) 


