price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

def calculate_discount(price, discount_percentage):
    if discount_percentage > 20:
        final_price = price - (price * discount_percentage / 100)
        return final_price
    else:
        final_price = price
        return final_price

print(f"The final price after discount is: {calculate_discount(price, discount_percentage)}")