# Write a python program that calculates the factorial of a given number.

def main():
    number = int(input("Enter a number: "))
    factorial = 1

    for i in range(1, number + 1):
        factorial *= i

    print(f"Factorial of {number} is: {factorial}")
main()