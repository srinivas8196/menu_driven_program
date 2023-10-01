def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def is_palindrome(s):
    s = s.lower()
    s = s.replace(" ", "")
    return s == s[::-1]

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            next_num = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_num)
        return fib_sequence

def table_of_number(n):
    table = []
    for i in range(1, 11):
        table.append(n * i)
    return table

while True:
    print("\nMenu:")
    print("1. Factorial")
    print("2. Palindrome")
    print("3. Fibonacci")
    print("4. Table of a Number")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        num = int(input("Enter a number to calculate its factorial: "))
        result = factorial(num)
        print(f"Factorial of {num} is {result}")
    
    elif choice == '2':
        string = input("Enter a string to check if it's a palindrome: ")
        if is_palindrome(string):
            print(f"{string} is a palindrome.")
        else:
            print(f"{string} is not a palindrome.")
    
    elif choice == '3':
        num = int(input("Enter the number of Fibonacci numbers to generate: "))
        result = fibonacci(num)
        print("Fibonacci Sequence:")
        print(result)
    
    elif choice == '4':
        num = int(input("Enter a number to generate its table: "))
        result = table_of_number(num)
        print(f"Table of {num}:")
        for i, value in enumerate(result, start=1):
            print(f"{num} x {i} = {value}")
    
    elif choice == '5':
        print("Exiting the program.")
        break
    
    else:
        print("Invalid choice! Please enter a valid option.")
