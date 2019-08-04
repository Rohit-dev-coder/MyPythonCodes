num = int(input("Enter a integers :"))
while num>0:
	print(num)
	nxt = 0
	rem = 0
	i=0
	while num>10:
		rem = num%10
		num = int(num/10)
		nxt = (rem * (10**i)) + nxt
		i = i + 1
	num=nxt