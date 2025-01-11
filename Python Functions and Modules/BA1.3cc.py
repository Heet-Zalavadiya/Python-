# Function to check if a string is a palindrome
def is_palindrome(s):
    # Loop through the string from both ends
    for i in range(len(s) // 2):
        # Compare characters from start and end
        if s[i] != s[len(s) - 1 - i]:
            return False  # If characters don't match, it's not a palindrome
    return True  # If all characters match, it is a palindrome

# Main program
if __name__ == "__main__":
    # Get input from user
    user_input = input("Enter a string: ")
    
    # Check if the string is a palindrome
    if is_palindrome(user_input):
        print(f"'{user_input}' is a palindrome.")
    else:
        print(f"'{user_input}' is not a palindrome.")
