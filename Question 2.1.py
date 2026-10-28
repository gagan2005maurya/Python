CORRECT_PIN = 1234
balance = 5000.0  # Initial account balance

entered_pin = int(input("Enter your 4-digit PIN: "))

if entered_pin == CORRECT_PIN:
  amount = float(input("Enter amount to withdraw: "))
  if amount % 100 == 0:
    if amount <= balance:
      balance -= amount
      print(f"Withdrawal successful! Remaining balance: {balance}")
    else:
      print("Insufficient Balance")
  else:
    print("Amount must be a multiple of 100.")
else:
  print("Invalid PIN")
  