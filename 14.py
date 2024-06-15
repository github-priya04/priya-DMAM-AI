# Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.
 

def read_and_print_lines():
    lines = []
    print("python is fun:")

    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    print("\n c is also fun:")
    for line in lines:
        print(line)

