def letter_occurrence(input_string):
    # complete function implementation...

    count = 0
    for char in input_string:
        if char =='a' or char =='A':
            count+=1
 

    return count
# Test the function with different strings
print(letter_occurrence("Abracadabra"))  # Output: 5
print(letter_occurrence("hello world"))  # Output: 0
print(letter_occurrence("Alabama"))      # Output: 4
print(letter_occurrence("AaaAaa"))       # Output: 6