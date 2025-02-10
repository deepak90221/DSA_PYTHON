
# Function to reverse a string
def reverse_string(s):
    return s[::-1]  # Slice the string in reverse order

# Example usage
if __name__ == "__main__":
    string = input()
    reversed_string = reverse_string(string)
    print("Original String:", string)
    print("Reversed String:", reversed_string)
