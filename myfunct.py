def myfunct(mylist):
	s = [x  for x in mylist]
	return s
text = input("Enter 5 no : ")
mylist=[]
for i in text:
	i=int(i)
  	mylist.append(i)
newlist = myfunct(mylist)
print(newlist)