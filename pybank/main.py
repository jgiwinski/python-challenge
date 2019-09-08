# import all the things! 
import os
import csv 

# declare all the columns
date = []
profLoss = []

# declare all the variables
totalMonths = 0
netTotal = 0
avgChange = 0
greatestIncreaseDate = ''
greatestIncreaseTotal = 0
greatestDecreaseDate = ''
greatestDecreaseTotal = 0
lineBreak = "-"*30

# path to collect all the things 
bankcsv = os.path.join('budget_data.csv') 

# create all the functions
def mean(numbers):
	return float(sum(numbers)) / max(len(numbers), 1)

# read csv file 
with open(bankcsv, newline='') as csvfile:
	reader = csv.DictReader(csvfile)

    # Iterating through each row
	for row in reader:
		# Tracking Date information
		date.append(row['Date'])
		# Tracking each individual change in Profits/Losses
		profLoss.append(int(row['Profit/Losses']))
	
		# Declaring variable to compare for greatest increase/decrease
		value = int(row['Profit/Losses'])
		# greatest increase 
		if greatestIncreaseTotal < value:
			greatestIncreaseTotal = value
			greatestIncreaseDate = row['Date']

		# greatest decrease 
		if greatestDecreaseTotal > value:
			greatestDecreaseTotal = value
			greatestDecreaseDate = row['Date']
		
		# total months
		totalMonths = totalMonths + 1
		# total of profits/losses
		netTotal = netTotal + int(row['Profit/Losses'])
        
# average change
avgChange = mean(profLoss)

# formatting average change, greatest increase/decrease, and net total
netTotal = "${:0,.2f}".format(netTotal)
avgChange = "${:0,.2f}".format(avgChange)
greatestIncreaseTotal = "${:0,.2f}".format(greatestIncreaseTotal)
greatestDecreaseTotal = "${:0,.2f}".format(greatestDecreaseTotal).replace('$-','-$')

# Stores all needed values in a variable for moving to a text file
txtFileInfo = f"Financial Analysis"'\n'f"{lineBreak}"'\n'f"Total months: {totalMonths}"'\n'f"Total: {netTotal}"'\n'f"Average Change: {avgChange}"'\n'f"Greatest increase in Profits: {greatestIncreaseDate} {greatestIncreaseTotal}"'\n'f"Greatest decrease in Profits: {greatestDecreaseDate} {greatestDecreaseTotal}"

# Prints requested variables to console
print(txtFileInfo)

textFile = open("bankFile.txt","w")
with open("bankFile.txt", "w") as att_file:
	att_file.write(txtFileInfo)