

mylist = []
text = input("Enter 5 int : ")
for x in text.split():
	mylist.append(int(x))
finallist = [ x for x in mylist if x != max(mylist) and x!=min(mylist) ]
print("list is ",mylist)
print("After ",finallist)