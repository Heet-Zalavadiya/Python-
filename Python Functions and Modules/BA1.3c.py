def is_palidrom(num):
    reverse=0
    while num!=0:
        digit=num%10
        reverse=reverse*10+digit
        num=num//10
    return reverse



if __name__ == "__main__":

    num = int(input("Enter value of number:"))
    n=num
    reverse = is_palidrom(num)
    if n==reverse:
        print('Given number is palidrom')
    else:
        print('Given number is not palidrom')
        


    


