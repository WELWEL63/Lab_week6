def is_happy_number(n):
    """
    Determine if a two-digit number is a happy number.
    
    Parameters:
    n (int): A positive integer with two digits.
    
    Returns:
    bool: True if the number is a happy number, False otherwise.
    """
    # Set to keep track of numbers we've already seen (to detect cycles)
    seen_numbers = set()
    
    while n != 1:
        # Split digits and calculate the sum of the square of each digit
        n = sum(int(digit) ** 2 for digit in str(n))
        
        # If we've already seen this number, we're in a cycle (unhappy number)
        if n in seen_numbers:
            return False
        seen_numbers.add(n)
    
    # If we reached 1, it's a happy number
    return True

# Test cases
print(is_happy_number(10))  # Expected output: True
print(is_happy_number(13))  # Expected output: True
print(is_happy_number(19))  # Expected output: True
print(is_happy_number(11))  # Expected output: False
print(is_happy_number(12))  # Expected output: False
print(is_happy_number(14))  # Expected output: False
