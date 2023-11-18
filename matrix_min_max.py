# This program prompts the user to input the dimensions of a matrix (rows and columns),
# fills the matrix with user-input integers, and then finds the minimum and maximum
# values for each row and column separately.


# Prompt the user to input the number of rows and columns for the matrix
r = int(input("Enter the number of rows: "))
c = int(input("Enter the number of columns: "))

# Initialize a matrix filled with zeros
matrix = [[0 for _ in range(c)] for _ in range(r)] 

# Fill the matrix by user-input integers
for i in range(r):
    for j in range(c):
        matrix[i][j] = int(input(f"Enter integer value at position [{i}][{j}]: "))

# Display the matrix
print(f"\nThe matrix {r}x{c}: ")
for row in matrix:
    print(row)

# Find minimum and maximum values in each row
for i in range(r):
    min_rows = matrix[i][0]    # Initialize minimum for the row 
    max_rows = matrix[i][0]    # Initialize maximum for the row    

    for j in range(c):
        # Update minimum and maximum values for the row
        min_rows = min(min_rows, matrix[i][j])
        max_rows = max(max_rows, matrix[i][j])

    # Display the minimum and maximum values for the row
    print(f"\nRow n°{i+1}")
    print(f"- The minimum in row {i+1} is {min_rows}")
    print(f"- The maximum in row {i+1} is {max_rows}")

    
# Find minimum and maximum values in each column
for j in range(c):
    min_cols = matrix[0][j]     # Initialize minimum for the column  
    max_cols = matrix[0][j]     # Initialize maximum for the column 

    for i in range(r):
        # Update minimum and maximum values for the column
        min_cols = min(min_cols, matrix[i][j])
        max_cols = max(max_cols, matrix[i][j])

    # Display the minimum and maximum values for the column
    print(f"\nColumn n°{j+1}")
    print(f"- The minimum in column {j+1} is {min_cols}")
    print(f"- The maximum in column {j+1} is {max_cols}")
