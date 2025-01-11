start=int(input("Enter the starting number of range:"))
end=int(input("Enter the ending number of range:"))

prime_sum=0

for num in range(start,end+1):
    is_prime=True

    if num>1:
        for i in range(2,num):
            if num % i ==0:
                is_prime=False
                break
    if is_prime==True:
        prime_sum+=num


print(f"The sum of all prime numbers between {start} and {end} is: {prime_sum}")







            
        
