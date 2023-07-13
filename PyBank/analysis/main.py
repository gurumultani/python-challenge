import os
import csv


#This will allow us to create file path across operating systems
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# Define the input file path
file_path = "budget_data.csv"

def analyse_financial_records(file_path):
    # Initialise variables
    total_months = 0
    net_total = 0
    previous_profit_loss = 0
    changes = []
    greatest_increase = ["", 0]
    greatest_decrease = ["", 0]

    # Read the CSV file
    with open(csvpath) as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)

        for row in csv_reader:
            # Update total months
            total_months += 1

            # Extract data from the row
            date = row[0]
            profit_loss = row[1]

            try:
                profit_loss = int(profit_loss)
            except ValueError:
                print(f"Skipping non-integer value in row {total_months + 1}")
                continue

            # Update net total
            net_total += profit_loss

            # Calculate the change in profit/losses
            change = profit_loss - previous_profit_loss

            # Update the previous profit/loss
            previous_profit_loss = profit_loss

            # Append the change to the list of changes
            if total_months > 1:
                changes.append(change)

            # Check for greatest increase/decrease
            if change > greatest_increase[1]:
                greatest_increase = [date, change]
            elif change < greatest_decrease[1]:
                greatest_decrease = [date, change]

    # Calculate the average change
    average_change = sum(changes) / len(changes)

    # Prepare the analysis summary
    analysis_summary = f"""
    Financial Analysis
    ----------------------------
    Total Months: {total_months}
    Total: ${net_total}
    Average Change: ${average_change:.2f}
    Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})
    Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})
    """

    return analysis_summary


# Analyse the financial records
summary = analyse_financial_records(file_path)
print(summary)

# Export the analysis summary to a text file
output_file_path = "financial_analysis.txt"
with open(output_file_path, 'w') as file:
    file.write(summary)

