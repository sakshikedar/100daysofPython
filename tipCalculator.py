print("Welcome to the tip genrator ")
bill = float(input("what was the total bill? Rs. "))

tip = int(input("what percentage tip? 10, 12 or 15?"))

bill_with_tip = tip /100 *bill +bill

split = int(input("how many people to split the bill? "))

result= bill_with_tip/split
res = round(result, 2)
print("each person should pay: Rs.",res)