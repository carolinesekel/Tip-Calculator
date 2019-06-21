from math import *

price = input("How much did your meal cost?\n")
price = float(price)

rating_to_percent = {
    "poor": .2,
    "fair": .2,
    "good": .2,
    "great": .25
}

rating = input("How was your service? (Enter poor, fair, good, or great)\n")

while rating not in rating_to_percent:
    rating = input("Error: Please enter poor, fair, good, or great.\n")

percent = rating_to_percent[rating]
            
ask_approval = "Tip " + str(percent*100) + "% ? (Enter yes or no)\n"
approval = input(ask_approval)

while approval=="no":
    percent = input("Enter a percentage to tip (Enter X for X% tip)\n")
    percent = int(percent)
    if percent < 20:
        print("Servers depend on tips for more than half of their total earnings.")
        if rating == "poor" or rating == "fair":
            print("Bad service is not an excuse not to tip - let a manager know if you had a bad experience, but don't harm your server's livelihood.")
        else:
            print("Wage theft is prevalent in the restaurant industry and servers often suffer minimum wage violations - not tipping adequately only furthers this problem.")
        answer = input("Are you sure you want to tip less than 20%?\n")
        if answer =="yes":
            ask_approval = "Tip " + str(percent) + "% ? (Enter yes or no)\n"
            approval = input(ask_approval)
            percent = percent/100
    else:
        ask_approval = "Tip " + str(percent) + "% ? (Enter yes or no)\n"
        approval = input(ask_approval)
        percent = percent/100

tip = round(price*percent , 2)
total = price+tip

if not total.is_integer():
    round_up = input("Round up to an even total?\n")
    if round_up =="yes":
        total = ceil(total)
        tip = total - price

print("Tip amount: %.2f" % tip)
print("Total: %.2f" % total)
    
