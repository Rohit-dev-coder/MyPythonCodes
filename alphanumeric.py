str = input("Enter AlphaNumeric String: ")
list = []
for x in str:
	if x in "1234567890":
		list.append(int(x))
print(sorted(list)) 