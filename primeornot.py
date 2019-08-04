print("\n********Check Prime or not********")
num = int(input("Enter Any Number: "))
i = 2
while i<num:
    if num%i == 0:
        print("{} is not a prime number".format(num))
        break
    i+=1
if i == num or num == 1:
    print("{} is prime number".format(num))
    