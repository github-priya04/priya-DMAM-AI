# Write a python program that returns the minimum and maximum values in a list of numbers.

num=int(input("enter n number:"))

arr=[]
for n in range (num):
    num2=int(input("enter number :"))
    arr.append(num2)                      
print(arr)
   

print("maximum value in the list is : ", max(arr))    
print("minimum value in the list is : ", min(arr))
      
     