x,y,z = input("Enter A Three Number: ").split()
print("Value of x is",x,"\nValue of y is",y,"\nValue of z is",z)
temp = x
x=y
y=z
z=temp 
print("Value of x is",x,"\nValue of y is",y,"\nValue of z is",z)
