import pandas as pd

myCsvPath = r'C:\Users\Julio\Downloads\Instructions\PyBank\Resources\budget_data.csv'

dfMonthlyPnL = pd.read_csv(myCsvPath)

# * The total number of months included in the dataset
numMonths = dfMonthlyPnL.shape[0]

# * The net total amount of "Profit/Losses" over the entire period
totalPnL = dfMonthlyPnL['Profit/Losses'].sum()

# * The average of the changes in "Profit/Losses" over the entire period
deltaMonthly = dfMonthlyPnL['Profit/Losses'].diff()

avgDeltaMonthly = deltaMonthly.mean()

# * The greatest increase in profits (date and amount) over the entire period
maxDeltaMonthly = deltaMonthly.max()
maxDeltaMonth = dfMonthlyPnL['Date'][deltaMonthly.idxmax()]

# * The greatest decrease in profits (date and amount) over the entire period
minDeltaMonthly = deltaMonthly.min()
minDeltaMonth = dfMonthlyPnL['Date'][deltaMonthly.idxmin()]

# * In addition, your final script should both print the analysis to the 
# terminal and export a text file with the results.
myOutPath = r'C:\Users\Julio\Desktop\PythonChallenge\PyBank\budget_analysis.txt'

f = open(myOutPath,'w+')

out = 'Financial Analysis\n----------------------------'
print(out)
f.write(out + '\n')

out = 'Total Months: %2d' %(numMonths)
print(out)
f.write(out + '\n')

out = 'Total: $%2d' %(totalPnL)
print(out)
f.write(out + '\n')

out = 'Average  Change: $%2.2f' %(avgDeltaMonthly)
print(out)
f.write(out + '\n')

out = 'Greatest Increase in Profits: {0} (${1:2.0f})'.format(maxDeltaMonth, maxDeltaMonthly)
print(out)
f.write(out + '\n')

out = 'Greatest Decrease in Profits: {0} (${1:2.0f})'.format(minDeltaMonth, minDeltaMonthly)
print(out)
f.write(out + '\n')

f.close()