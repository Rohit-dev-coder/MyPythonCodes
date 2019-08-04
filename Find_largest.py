def find_largest(*str):
	max = 0
	for i in str:
		if len(i)>max:
			max = len(i)
			s = i
	return max,s
print(find_largest("rohit","siddhi","kiran"))
print(find_largest("one","two","three","four","five","six"))