# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇

print("Welcome to Tip Calculator 101!")

bill = float(input("What is the bill? \n$"))
tip = float(input("Would you like to tip 10, 12 or 15 percent? \n"))
people = int(input("How many people are splitting the bill?\n"))
totalBill = bill * (1 + (tip / 100))
# something new -- formating to decimal places
dividedBill = "{:.2f}".format(round(totalBill / people, 2))

print(f"Each person should pay ${dividedBill}")
