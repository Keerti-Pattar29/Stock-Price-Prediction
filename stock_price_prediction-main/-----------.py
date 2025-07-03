import pandas as pd

# Read stock data from a CSV file
file_path = 'path_to_your_stock_data.csv'  # Replace with your file path
stock_data = pd.read_csv(file_path)

# Convert the DataFrame to a NumPy array
stock_array = stock_data.to_numpy()

# Print the array
print(stock_array)
