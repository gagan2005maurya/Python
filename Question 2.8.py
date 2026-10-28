experience = float(input("Enter employee experience (in years): "))
salary = float(input("Enter employee salary (₹): "))
performance = float(input("Enter employee performance score: "))

bonus_percentage = 0

if experience >= 1 and salary >= 50000:  #[span_7](start_span)[span_7](end_span)
  if performance >= 90:  #[span_8](start_span)[span_8](end_span)
    bonus_percentage = 20  #[span_9](start_span)[span_9](end_span)
  elif performance >= 75:  #[span_10](start_span)[span_10](end_span)
    bonus_percentage = 10  #[span_11](start_span)[span_11](end_span)
  else:
    bonus_percentage = 5  # Otherwise -> 5% bonus[span_12](start_span)[span_12](end_span)
elif salary < 50000:  #[span_13](start_span)[span_13](end_span)
  if performance >= 90:  #[span_14](start_span)[span_14](end_span)
    bonus_percentage = 15  #[span_15](start_span)[span_15](end_span)
  else:
    bonus_percentage = 5  # Otherwise -> 5% bonus[span_16](start_span)[span_16](end_span)
else:
  bonus_percentage = 5

bonus_amount = (salary * bonus_percentage) / 100
print(f"Bonus Percentage: {bonus_percentage}%")
print(f"Bonus Amount: ₹{bonus_amount:.2f}")
