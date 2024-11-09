#def is_golden_number(n):
#     # function implementation ...
    
def is_golden_number(n):
    # Loop through all possible values of a where a + b = n
    for a in range(1, n):
        b = n - a  # Since a + b = n, b is calculated as n - a
        
        # Check if the product of a and b is divisible by 1000
        if a * b % 1000 == 0:
            return True
    
    # If no such pair (a, b) is found, return False
    return False
# Test cases
print(is_golden_number(65))  # Expected output: True (since 65 = 40 + 25 and 40 * 25 = 1000)
print(is_golden_number(70))  # Expected output: True (since 70 = 20 + 50 and 20 * 50 = 1000)
print(is_golden_number(123))  # Expected output: False (no pair with product divisible by 1000)
print(is_golden_number(500))  # Expected output: False (no pair with product divisible by 1000)
