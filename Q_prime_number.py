num=int(input("Please enter number: "))

for i in range(2,num):
    if num % i==0:
        print("Not a prime number")
        exit()

print("Prime number")