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
#print(rating)

while rating not in rating_to_percent:
    rating = input("Error: Please enter poor, fair, good, or great.\n")

percent = rating_to_percent[rating]
            
ask_approval = "Tip " + str(percent*100) + "% ? (Enter yes or no)\n"
approval = input(ask_approval)

if approval=="no":
    go = True
    while go:
        percent = input("Enter a percentage to tip (Enter X for X% tip)\n")
        percent = int(percent)
        if percent < 20:
            #print fact 
            answer = input("Are you sure you want to tip less than 20%?\n")
            if answer =="yes":
                #print rude message
                ask_approval = "Tip " + str(percent) + "% ? (Enter yes or no)\n"
                approval = input(ask_approval)
                percent = percent/100
                go = False
        else:
            ask_approval = "Tip " + str(percent) + "% ? (Enter yes or no)\n"
            approval = input(ask_approval)
            percent = percent/100
            go = False

if approval == "yes":
    tip = round(price*percent , 2)
    total = price+tip

    if not total.is_integer():
        round_up = input("Round up to an even total?\n")
        if round_up =="yes":
            total = ceil(total)
            tip = total - price
    
    print("Tip amount: %.2f" % tip)
    print("Total: %.2f" % total)
        
