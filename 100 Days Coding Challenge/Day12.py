# Write a program to find Sum of digits of a number
num=int(input("Enter a number: "))
Sum=0
while num!=0:
    Sum=Sum+num%10
    num=num//10
print(Sum)