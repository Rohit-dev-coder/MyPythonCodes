while(True):
	try:
		a=int(input("Input first no:"))
		b=int(input("Input second no:"))
		c=a/b
		print("Div is ",c)
		break;
	except (ValueError,ZeroDivisionError):
		print("Either input is incorrect or denominator is 0. Try again!")	
