cart_amount = float(input("Enter cart amount (₹): "))
is_premium = (
    input("Is the customer a premium member? (yes/no): ").strip().lower()
)

if cart_amount >= 5000:
  if is_premium == "yes":
    discount_percentage = 20
  else:
    discount_percentage = 10
else:
  if is_premium == "yes":
    discount_percentage = 5
  else:
    discount_percentage = 0

discount_amount = (cart_amount * discount_percentage) / 100
final_amount = cart_amount - discount_amount

print(f"Discount applied: {discount_percentage}%")
print(f"Final amount to pay: ₹{final_amount:.2f}")
