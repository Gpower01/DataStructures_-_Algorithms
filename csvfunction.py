#create stockprices.csv

import csv

data = [
    ["Date", "Value"],
    ["6-Mar", 310],
    ["7-Mar", 340],
    ["8-Mar", 380],
    ["9-Mar", 302],
    ["10-Mar", 297],
    ["11-Mar", 323],
    ]

with open ("stock_prices.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)



