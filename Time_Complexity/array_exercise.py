# Monthly spend list for the first five months
months = [2200, 2350, 2600, 2130, 2190]

# 1. Calculate the amount of dollars spent extra in February compared to January
feb_extra_spend = months[1] - months[0]
print(f"February spend was greater than January by: ${feb_extra_spend}")

# 2. Calculate the total amount spent in the first Quarter (first three months) of the year
total_first_quarter = sum(months[:3])
print(f"Total spend in the first quarter: ${total_first_quarter}")

# 3. Check if we spent exactly 2000 dollars in any month
spent_2000 = 2000 in months
if spent_2000:
    print("We spent exactly $2000 in one of the months.")
else:
    print("We did not spend exactly $2000 in any month.")

# 4. June month just finished and the expense was 1980 - add this amount to monthly spend list
months.append(1980)
print(f"Monthly spend list after adding June: {months}")

# 5. In April, an item was returned and a refund was issued for an amount of $20. Adjust April monthly spend
# April is the fourth month, index 3
months[3] += 20
print(f"Monthly spend list after refund in April: {months}")
