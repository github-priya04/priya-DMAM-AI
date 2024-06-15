# Write a python program that calculates the sum of the digits of a given number.

i=int(input("enter number"))
sum=0
while(i>0):
    sum=sum+i%10
    i=i//10
print("sum of digits=",sum)


