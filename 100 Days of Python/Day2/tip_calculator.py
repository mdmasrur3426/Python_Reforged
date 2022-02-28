print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? "))
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people_count = int(input("How many people to split the bill? "))
tip_percent /= 100
tip = total_bill * tip_percent
total_bill += tip
per_bill = round(total_bill/people_count, 2)
per_bill = "{:.2f}".format(per_bill)
print(f"Each person should pay: ${per_bill}")