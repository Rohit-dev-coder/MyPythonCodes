text = input("Type 5 integers:")
mylist = [int(x) for x in text.split()]
print("list is ",mylist)
print("sum is ",sum(mylist))