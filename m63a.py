#•	Write a Python program to returns sum of all divisors of a number

prompt = int(input("Enter an interger: "))

print("The divisors of the integer you entered are: ")
for i in range(1, prompt+1):
    if(prompt%i==0):
        print(i)
