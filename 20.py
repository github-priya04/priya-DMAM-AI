# Write a python program that takes a list of numbers and returns their sum.

def sum_list(my_list):
     temp=0
     for item in my_list:
          temp= temp+item
          return temp
      
l = int(input("Enter list length:"))
numbers_list=[]   
for _ in range(l):
   temp=int(input("Enter list item:"))
   numbers_list.append(temp)

total=sum_list(numbers_list)
print("Sum of all the numbers in list is:",total)
        

