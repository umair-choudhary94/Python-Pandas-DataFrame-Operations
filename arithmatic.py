# Import the pandas library and alias it as 'pd'
import pandas as pd

# Create a DataFrame 'var' with two columns 'A' and 'B' using a dictionary
var = pd.DataFrame({"A":[3,4,5,6,7],"B":[7,3,8,9,7]})

# Print the initial DataFrame 'var'
print(var)

# Performing arithmetic operations and adding new columns to the DataFrame 'var'

# Add a new column 'sum' that contains the sum of columns 'A' and 'B'
var["sum"] = var["A"] + var["B"]
print(var)

# Add a new column 'Subtract' that contains the result of subtracting column 'B' from column 'A'
var["Subtract"] = var["A"] - var["B"]
print(var)

# Add a new column 'multiply' that contains the product of columns 'A' and 'B'
var["multiply"] = var["A"] * var["B"]
print(var)

# Add a new column 'division' that contains the result of dividing column 'A' by column 'B'
var["division"] = var["A"] / var["B"]
print(var)

# Condition Checking

# Add a new column 'Condition' that checks if each value in column 'A' is greater than or equal to 5
var["Condition"] = var["A"] >= 5
print(var)
