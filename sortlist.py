i=1
sortednums=[]
print("Enter any 5 random integers:")
while i<=5:
	n=int(input())
	pos=0
	for x in sortednums:
		if x>n:
		   break
		pos=pos+1   	
	sortednums.insert(pos,n)
	i=i+1
print("Sorted list is:")
print(sortednums)
				
	