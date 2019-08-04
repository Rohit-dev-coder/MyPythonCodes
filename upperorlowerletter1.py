ch = ord(input("Enter A character: "))
if ch>=65 and ch<=90 :
	print("uppercase")
elif ch>=97 and ch<=122 :
	print("Lowercase")
elif ch>=48 and ch<=57 :
	print("Number")
else:
	print("Special character")