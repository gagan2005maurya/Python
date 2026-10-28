age = int(input("Enter your age: "))

if age >= 21:
  salary = float(input("Enter your salary (₹): "))
  if salary >= 25000:
    credit_score = int(input("Enter your credit score: "))
    if credit_score >= 750:
      print("Loan approved.")
    elif credit_score >= 650:
      print("Loan approved with higher interest.")
    else:
      print("Loan rejected.")
  else:
    print("Loan rejected: Salary is below ₹25,000.")
else:
  print("Loan rejected: Age must be at least 21.")
  