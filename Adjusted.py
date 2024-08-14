# Define the function to calculate Adjusted R-squared
def adjusted_r_squared(r_squared, n, k):
    """
    Calculate the Adjusted R-squared value.

    Parameters:
    r_squared (float): The R-squared value.
    n (int): The number of observations.
    k (int): The number of predictors.

    Returns:
    float: The Adjusted R-squared value.
    """
    return 1 - ((1 - r_squared) * (n - 1) / (n - k - 1))

# Given values
r_squared_value = 0.75
n_obs = 100
n_pred = 3

# Calculate the Adjusted R-squared
result = adjusted_r_squared(r_squared_value, n_obs, n_pred)

# Print the results
print("Adjusted R-squared:", result)
print("Reg No: 11162220118")
