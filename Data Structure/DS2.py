def avg_of_numbers(number):
    total = 0
    count = 0
    for num in number:
        total+=num
        count = count + 1
    avg = total/count
    return avg

def sum_of_numbers(number):
    total = 0
    for num in number:
        total+=num
    return total

    



if __name__ == "__main__":

    user_input = input("Enter a list of number separated by space: ")

    number=[]

    for x in user_input.split():
        number.append(int(x))

    result = avg_of_numbers(number)
    total = sum_of_numbers(number)

    print(result)
    print(total)

