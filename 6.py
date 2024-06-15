# Write a program that reads the content of a text file and prints it to the console.

def creation():
    name = input("Enter the file name to create: ")
    file = open(name, 'w')
    text = input("Enter text to add to the file: ")
    file.write(text)
    file.close()
    print("File",name,"created successfully.")

def reading():
    name = input("Enter the file name to read: ")
    file = open(name, 'r')
    print(file.read())
    file.close()

def main():
    print("1. Create a new file and add text to it")
    print("2. Read an existing file")
    choice = input("Enter your choice: ")

    if choice == '1':
        creation()
    elif choice == '2':
        reading()
    else:
        print("Invalid choice.")

main()