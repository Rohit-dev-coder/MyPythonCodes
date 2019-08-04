def factorial (i):
	fact =1
	while i>0:
		fact=fact*i
		i-=1
	return fact
i = int(input("Enter a number :"))
print(factorial(i))