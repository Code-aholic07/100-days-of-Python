print("Welcome to Tip Calculator")
total=float(input("Enter the total bill amount"))
tip=int(input("Enter the tip percentage you would like to give\n 10, 12 or 15?"))
div=int(input("How many people are splitting the bill?"))
if tip==10 or tip==12 or tip==15:
    print("Each person should pay",(total+(tip/100*total))/div)
else:
    print("Valid tip amount wasn't provided")
