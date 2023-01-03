print("Welcome to the tip calculator")
Total_bil = int(input("What's the total bill? "))
Bill_spill = int(input("How many people to split the bill? "))
Percentage = int(input("What percentage will you like to split the bill? 10, 12, or 15? "))
if Percentage == 12:
    Price = (Total_bil / Bill_spill) * 1.12
    Price_in_2dp = "{:.2f}".format(Price)
    Message = f"Each person should pay: {Price_in_2dp}"
    print(Message)
elif Percentage == 15:
    Price = (Total_bil / Bill_spill) * 1.15
    Price_in_2dp = "{:.2f}".format(Price)
    Message = f"Each person should pay: {Price_in_2dp}"
    print(Message)
else:
    Price = (Total_bil / Bill_spill) * 1.1
    Price_in_2dp = "{:.2f}".format(Price)
    Message = f"Each person should pay: {Price_in_2dp}"
    print(Message)
