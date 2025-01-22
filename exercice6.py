price = int(input("Enter the price: "))
discount = price * 0.15
tax = price * 0.20
if price >= 200:
    total_price = price - discount + tax
else:
    total_price = price + tax
print(f"The total price is: {total_price}")
