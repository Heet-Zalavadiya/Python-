num_terms=int(input("Enter number of terms for Fibonacci sequence:"))
a,b=0,1
print("Fibonacci sequence up to",num_terms,"terms:")
for _ in range(num_terms):
    print(a,end=" ")
    a,b=b,a+b
      
