import sys
def view_country(country):
	for x in sorted(country):
		print(x,end=" ")
	print()
	code = input("Enter Country code:").upper()
	x = country.get(code,-1)
	if x != -1:
		print("Country is",x)
	else:
		print("Invalid code")
		
def add_country(country):
	code = input("Enter Country Code: ").upper()
	if(code in country):
		print("Code already Present")
		return
	name = input("Enter Country Name: ")
	add = {code:name}
	country.update(add)
	print("{} added to the list".format(name))
def del_country(country):
	code = input("Enter Country Code: ")
	x = country.pop(code,-1)
	if x == -1:
		print("Country Code not Found!!")
	else:
		print("Delete Sucessfully!!..")

country = {"IN" : "India", "US":"America", "AU": "Australia","CA":"Canada"}
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