# Write a python program that checks whether a given number is even or odd.

def check(num): 
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
num=int(input("Enter your number :"))
final=check(num)
print("your number",num, "is",final)
    
    
    
    
    
    
    
    
