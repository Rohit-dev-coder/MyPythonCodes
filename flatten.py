def flatten(mylist):
	newlist = [y for x in mylist for y in x]	
	return newlist
mylist = [[1,3,4],[1,34,67],[32,1],[34,56,4]]
print(mylist)
print(flatten(mylist))

