def Add(numbers: str) -> int:
    # Return 0 for empty string
    if numbers == "":
        return 0

    # Split by comma
    parts = numbers.split(',')

    if len(parts) > 2:
            raise ValueError("Only up to two numbers are allowed")

    # Sum up to two numbers (gracefully handles 1 or 2 numbers)
    total = 0
    for part in parts:
        if part.strip():  # skip empty entries
            total += int(part.strip())
    return total

# Example usage
print(Add(""))          # Output: 0
print(Add("1"))         # Output: 1
print(Add("1,2"))       # Output: 3
print(Add("1,2,3,4"))   # Output: ValueError: Only up to two numbers are allowed
