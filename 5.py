# Write a program that takes a string input from the user and writes it to a text file.

string = input("Enter a string : ")
file=open("output.txt","w")
file.write(string)
file.close()

print("The value has been written to output.txt")

