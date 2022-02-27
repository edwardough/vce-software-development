number = int(input("Enter a number "))  
for i in range(number - 1):
    num = i + 1
    factorial = number * num
    number = factorial
    print(factorial)   

