import os
import csv

file_to_load = "PyBank/Resources/budget_data.csv"
total_months = 1 
sum_of_changes = 0
change_list =[]
profit_loss = None 
with open(file_to_load) as financial_data: 
    reader = csv.reader(financial_data)
    #skip header
    header = next(reader)
    first_row= next(reader)
    prev_net = int(first_row[1])
    prev_val = int(first_row[1])
    sum_of_changes = int(first_row[1])
    for row in reader:
        total_months += 1 
        sum_of_changes += int(row[1])
        change_list += [ int(row[1]) - int(prev_val)]
        prev_net += int(row[1])
        prev_val = int(row[1])
average_of_changes = sum(change_list)/len(change_list)
greatest_profit = max(change_list) 
greatest_loss = min(change_list) 
print('Total Months:', total_months)
print('Total:', sum_of_changes)
print('average_of_changes is: ' , '${:.2f}'.format(average_of_changes))
print('Greatest Increase in Profits:', '${:.0f}'.format(greatest_profit))
print('Greatest Decrease in Profits:', '${:.0f}'.format(greatest_loss))

