sum=0
while True:
	n = int(input("Enter a integers (0 for stop): "))
	if n==0:
		break
	elif n<0:
		continue 
	sum = sum+n
print("Sum of integers is",sum)	