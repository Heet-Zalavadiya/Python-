def fibonacci(n):
 
    if n<=1:
        return n
    else:

        return fibonacci(n-1)+fibonacci(n-2)

def fibonacci_sequence(n):

    return [fibonacci(i) for i in range(n)]

n=5
print(f"Fibonacci sequence up to {n} terms:{fibonacci_sequence(n)}")
