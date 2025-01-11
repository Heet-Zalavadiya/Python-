total_sum=0
while True:
    num=int(input("Enter a number:"))

    if num<0:
        print("Negative number is encountered so stopping the sum.")
        break

    total_sum+=num

print(f"The total sum of number is:{total_sum}")
