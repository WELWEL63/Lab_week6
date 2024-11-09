import random

# Function 1: create_2d_list
def create_2d_list(n):
    """Creates an n x n 2D list with random integers between 1 and 10."""
    return [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]

# Function 2: row_col_max
def row_col_max(list_2d):
    """Finds the row and column indices of the maximum number in the 2D list."""
    max_value = -1
    max_row = -1
    max_col = -1

    # Iterate through the 2D list and find the maximum value's indices
    for row_idx, row in enumerate(list_2d):
        for col_idx, value in enumerate(row):
            if value > max_value:
                max_value = value
                max_row = row_idx
                max_col = col_idx

    return max_row, max_col

# Function 3: is_win
def is_win(row, column):
    """Checks if the sum of row and column indices is less than or equal to 3."""
    return (row + column) <= 3

# Function 4: main
def main():
    # Step 1: Prompt the user for the size of the 2D list
    n = int(input("Enter the size of the 2D list (must be greater than 5): "))
    
    # Step 2: Validate input size
    if n <= 5:
        print("Please enter a size greater than 5.")
        return
    
    # Step 3: Create the 2D list using the create_2d_list function
    list_2d = create_2d_list(n)
    
    # Step 4: Display the created 2D list for the user to see
    print("The generated 2D list is:")
    for row in list_2d:
        print(row)

    # Step 5: Find the row and column indices of the maximum number
    max_row, max_col = row_col_max(list_2d)
    
    # Step 6: Check if the user wins using the is_win function
    if is_win(max_row, max_col):
        print(f"Congratulations! You win! The maximum number is at position ({max_row}, {max_col}).")
    else:
        print(f"Sorry! You did not win. The maximum number is at position ({max_row}, {max_col}).")

# Run the program
if __name__ == "__main__":
    main()
