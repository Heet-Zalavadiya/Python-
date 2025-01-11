def input_matrices(rows, col):
    N=[]
    print("Enter value of matrix :")
    for i in range(row):
        row_elements=[]
        for j in range(col):
            value=int(input(f"Enter value for [{i+1}][{j+1}]:"))
            row_elements.append(value)
        N.append(row_elements)

    return N
def add_matrices(A, B, row, col):
    """Function to add two matrices A and B."""
    result = []
    for i in range(row):
        row_result = []
        for j in range(col):
            row_result.append(A[i][j] + B[i][j])
        result.append(row_result)
    return result

def substract_matrices(A, B, row, col):
    result1=[]
    for i in range(row):
        row_result=[]
        for j in range(col):
            row_result.append(A[i][j] - B[i][j])
        result1.append(row_result)
    return result1

def multiplication_matrices(A, B, row, col):
    result2=[]
    for i in range(row):
        row_result=[]
        for j in range(col):
            sum=0
            for k in range(col):
                sum += A[i][k] * B[k][j]
            row_result.append(sum)
        result2.append(row_result)
    return result2



if __name__ == "__main__":

    row = int(input("Enter the number of rows: "))
    col = int(input("Enter the number of columns: "))

    A = input_matrices(row, col)
    B = input_matrices(row, col)

    result = add_matrices(A, B, row, col)
    result1 = substract_matrices(A, B, row, col)
    result2 = multiplication_matrices(A, B, row, col)

    print("Addition of Matrix A and Matrix B:")
    for i in range(row):
        for j in range(col):
            print(result[i][j], end=" ")
        print()


    print("Substraction of Matrix A and Matrix B:")
    for i in range(row):
        for j in range(col):
            print(result1[i][j], end=" ")
        print()


    print("Multiplication of Matrix A and Matrix B:")
    for i in range(row):
        for j in range(col):
            print(result2[i][j], end=" ")
        print()
            
                  




