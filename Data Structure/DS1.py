def sum_of_even_numbers(number):
    total=0
    for num in number:
        if num%2 == 0:
            total +=num
    return total

if __name__ == "__main__":

    user_input = input("Enter a list of number separated by space: ")

    number = []

    for x in user_input.split():
        number.append(int(x))


    result = sum_of_even_numbers(number)

    print(f"The sum of the even numbers in the list is: {result}")
    
