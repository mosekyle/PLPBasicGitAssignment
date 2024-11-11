def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user for input
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate and display the final price
    final_price = calculate_discount(price, discount_percent)
    print(f"The final price after applying the discount is: ${final_price:.2f}")
except ValueError:
    print("Please enter valid numerical values for price and discount.")


# Function Definition:
# The function calculate_discount accepts price and discount_percent as parameters.
# If the discount_percent is 20% or higher, it applies the discount.
# Otherwise, it returns the original price without modification.
# User Input and Display:

# Prompts the user to enter price and discount_percent.
# Calls the calculate_discount function with the user inputs.
# Prints the final price, formatted to two decimal places, if a discount was applied; otherwise, it prints the original price.
