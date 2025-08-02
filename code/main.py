def Add(numbers: str) -> int:
    # Return 0 for empty string
    if numbers == "":
        return 0

    # Raise error if input ends with a newline
    if numbers.endswith('\n'):
        raise ValueError("Input should not end with a newline character")

    # Replace newlines with commas
    numbers = numbers.replace('\n', ',')

    # Split by comma
    parts = numbers.split(',')

    # Sum of all the numbers in input string
    total = 0
    for part in parts:
        if part.strip():  # skip empty entries
            total += int(part.strip())
    return total

# Example usage
print(Add(""))              # Output: 0
print(Add("1"))             # Output: 1
print(Add("1,2"))           # Output: 3
print(Add("1,2,3,4"))       # Output: 10
print(Add("1\n2,3"))        # Output: 6
print(Add("1,2\n"))         # ValueError: Input should not end with a newline character
