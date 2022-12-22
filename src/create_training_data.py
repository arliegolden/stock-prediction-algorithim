import yfinance as yf
import csv
import os

ticker = input("Input ticker: ")

# Get the stock data for the stock
stock = yf.Ticker(ticker)

# Get the historical data for the stock
historical_data = stock.history(start="2021-11-22", end="2022-11-22", interval="1d")

# Save the data to a CSV file
historical_data.to_csv(ticker + "_stock_data.csv")

print("Successfully Downloaded Stock CSV!")

# Open the input and output files
with open(ticker + "_stock_data.csv", "r") as in_file, open("Stock_training_data.csv", "w", newline="") as out_file:
    # Create CSV readers and writers
    reader = csv.reader(in_file)
    writer = csv.writer(out_file)

    # Write the header row to the output file
    header = next(reader)
    header.append("target")
    writer.writerow(header)

    # Iterate over the rows in the input file
    for row in reader:
        open_price = float(row[1])
        close_price = float(row[4])

        # Set the target value to 1 if the open price is smaller than the close price, 0 otherwise
        if open_price < close_price:
            target = 1
        else:
            target = 0

        # Write the row to the output file
        row.append(target)
        writer.writerow(row)

    print("Successfully calculated target position and added data to table!")

    # Open the file for reading
    with open("Stock_training_data.csv", "r") as f:
        # Read the contents of the file
        contents = f.read()

        # Lowercase the contents of the file
        lowercase_contents = contents.lower()
       

    # Open the file for writing
    with open("Stock_training_data.csv", "w") as f:
        # Write the lowercased contents to the file
        f.write(lowercase_contents)
       
    # Open the file for reading
    with open("Stock_training_data.csv", "r") as f:
        # Read the contents of the file
        contents = f.read()

        # Replace "datetime" with "date" in the contents of the file
        modified_contents = contents.replace("datetime", "date")

    # Open the file for writing
    with open("Stock_training_data.csv", "w") as f:
    # Write the modified contents to the file
        f.write(modified_contents)

        print("Successfully reformatted table for ML training!")

    if os.path.exists(ticker + "_stock_data.csv"):
        os.remove(ticker + "_stock_data.csv")

    print("Success! CSV table should be in the folder this script is in, with the name: training_data.csv")

 

        

