#incomplete code 
n = input("Enter a Number:")
i=0
numbers = {0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten"}
for x in n:
	mul = len(n)-i
	if(mul == 2 and int(n)>20):
		print(numbers.get(int(x)),"ty",end="",sep="")
	elif(mul == 1 or int(n)<=20 and mul!=2):
		if(int(n)>10 and int(n)<20):
			print(numbers.get(int(x)),"teen",end="",sep="")
			i+=1
			continue
		print(numbers.get(int(x)),end="")
	i+=1
		
		
		
