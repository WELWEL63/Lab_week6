def find_maximum_difference(a, b):
#     # code implementation here...

    # Initialize the variable to store the maximum difference
    maximum = 0
    
    # Iterate over both lists using zip() to pair up corresponding elements
    for num1, num2 in zip(a, b):
        # Calculate the absolute difference between the two elements
        diff = abs(num1 - num2)
        
        # Update the maximum if the current difference is greater
        if diff > maximum:
            maximum = diff
    
    # Return the maximum difference
    return maximum

print(find_maximum_difference([1, 5, 600], [100, 7, 3, 29, 39]))  
print(find_maximum_difference([1,5 ,600], [110 ,61, 3 , 701, 29]))


