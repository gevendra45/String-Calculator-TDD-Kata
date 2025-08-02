def Add(numbers: str) -> int:
    # Return 0 for empty string
    if numbers == "":
        return 0

    delimiter = [',', '\n']

    # Raise error if input ends with a newline
    if numbers.endswith('\n'):
        raise ValueError("Input should not end with a newline character")

    # Check if custom delimiter is specified at the start: "//[delimiter]\n"
    if numbers.startswith("//"):
        delimiter_line, numbers = numbers.split('\n', 1)
        # Extract single character delimiter after "//"
        custom_delim = delimiter_line[2:]
        if not custom_delim:
            raise ValueError("Custom delimiter missing after '//'")
        delimiter = [custom_delim]

    # Replace delimiter with commas
    for i in delimiter:
        numbers = numbers.replace(i, ',')

    # Split by comma
    parts = numbers.split(',')

    # Sum of all the numbers in input string
    total = 0
    negatives = []

    for part in parts:
        part = part.strip()
        if part: # skip empty entries
            num = int(part)
            if num < 0:
                negatives.append(num)
            else:
                total += num

    # If any negatives found, raise error listing them
    if negatives:
        raise ValueError(f"negatives not allowed: {', '.join(map(str, negatives))}")
    return total

# Example usage
print(Add(""))              # Output: 0
print(Add("1"))             # Output: 1
print(Add("1,2"))           # Output: 3
print(Add("1,2,3,4"))       # Output: 10
print(Add("1\n2,3"))        # Output: 6

try:
    print(Add("1,2\n"))
except ValueError as e:
    print(e)  # Output: negatives not allowed: -2, -4

print(Add("//;\n1;2"))      # Output: 3

try:
    print(Add("//;\n1;2\n"))
except ValueError as e:
    print(e)  # Output: Input should not end with a newline character

try:
    print(Add("1,-2,3,-4"))
except ValueError as e:
    print(e)  # Output: Input should not end with a newline character

try:
    print(Add("//;\n1;-2;3;-4"))
except ValueError as e:
    print(e)  # Output: negatives not allowed: -2, -4
