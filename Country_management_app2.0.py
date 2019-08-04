import sys
def view_country(country):
	for x in sorted(country):
		print(x,end=" ")
	print()
	code = input("Enter Country code:").upper()
	x = country.get(code,-1)
	if x != -1:
		print("Country is",x[0])
		print("Country Capital is",x[1])
		print("Country Population is",x[2])
	else:
		print("Their is no country for country code",code)
		
def add_country(country):
	code = input("Enter Country Code: ").upper()
	if(code in country):
		print("Code already Present")
		return
	list = []
	list.append(input("Enter Country Name: "))
	list.append(input("Enter Country Capital: "))
	list.append(input("Enter Country population: "))
	add = {code:list}
	country.update(add)
	print("{} added to the list".format(list[0]))
def del_country(country):
	code = input("Enter Country Code: ").upper()
	x = country.pop(code,-1)
	if x == -1:
		print("Country Code not Found!!")
	else:
		print("Delete Sucessfully!!..")

country = {"IN" : ["India","Delhi",13200000000], "US":["America","Washington",32000000000], "AU": ["Australia","Canberra",2410000000],"CA":["Canada","Ottawa",94000]}
while True:
	print("SELECT AN OPTION: ")
	print("View: View country names")
	print("add: Add a country")
	print("del: Delete a country")
	print("exit: Exit the program")
	choice = input().lower()
	if(choice == "view"):
		view_country(country)
	elif(choice == "add"):
		add_country(country)
	elif(choice == "del"):
		del_country(country)
	elif(choice == "exit"):
		sys.exit(0)
	else:
		print("Wrong Choice..!!")
		print("Try Again..")
	print()