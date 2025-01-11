def factorial(num):
    fact=1
    i=1
    while i<=num:
        fact=fact*i
        i=i+1
    return fact

    
if __name__ == "__main__":

    num = int(input("Enter value of number:"))

    fact = factorial(num)


print(f"The factorial of {num} is {fact}")
