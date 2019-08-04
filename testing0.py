abc = 101
while (abc < 1000):
	c = abc%10
	ccc = (c*100)+(c*10)+c
	if (abc+abc+abc) == ccc:
		print(abc)
	abc+=1