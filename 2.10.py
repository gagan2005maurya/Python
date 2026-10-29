# Predefined account details for simulation
correct_pin = 1234
is_active = True  # Account must be active[span_20](start_span)[span_20](end_span)
account_balance = 25000

entered_pin = int(input("Enter your 4-digit PIN: "))

if entered_pin == correct_pin:  # PIN must be correct[span_21](start_span)[span_21](end_span)
  if is_active:
    amount = float(input("Enter withdrawal amount (₹): "))
    if amount > 0:  # Amount must be positive[span_22](start_span)[span_22](end_span)
      if amount % 100 == 0:  # Amount must be a multiple of ₹100[span_23](start_span)[span_23](end_span)
        # Balance must be sufficient and minimum balance of ₹500 must remain[span_24](start_span)[span_24](end_span)
        if account_balance - amount >= 500:
          if amount > 20000:  # Amount > ₹20,000 -> Extra verification[span_25](start_span)[span_25](end_span)
            print("Amount exceeds ₹20,000. Extra verification required.")
            verification = (
                input("Did you pass verification? (yes/no): ").strip().lower()
            )
            if verification != "yes":
              print("Transaction cancelled due to failed extra verification.")
              exit()

          account_balance -= amount
          print(
              f"Please collect your cash: ₹{amount}. Remaining balance:"
              f" ₹{account_balance}"
          )
        else:
          print(
              "Withdrawal failed: Insufficient balance or minimum ₹500 balance"
              " requirement not met."
          )
      else:
        print("Withdrawal failed: Amount must be a multiple of ₹100.")
    else:
      print("Withdrawal failed: Amount must be positive.")
  else:
    print("Withdrawal failed: Account is not active.")
else:
  print("Withdrawal failed: Incorrect PIN.")
  