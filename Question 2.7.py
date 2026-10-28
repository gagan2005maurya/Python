units = float(input("Enter total units consumed: "))
bill = 0

if units <= 100:
  bill = units * 5  # ₹5/unit[span_2](start_span)[span_2](end_span)
elif units <= 200:
  bill = (100 * 5) + ((units - 100) * 7)  # ₹7/unit[span_3](start_span)[span_3](end_span)
elif units <= 300:
  bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)  # ₹10/unit[span_4](start_span)[span_4](end_span)
else:
  bill = (
      (100 * 5) + (100 * 7) + (100 * 10) + ((units - 300) * 15)
  )  # ₹15/unit[span_5](start_span)[span_5](end_span)

# Additionally, if bill > ₹3,000, add a 10% surcharge[span_6](start_span)[span_6](end_span)
if bill > 3000:
  surcharge = bill * 0.10
  bill += surcharge
  print(f"10% surcharge added. Surcharge amount: ₹{surcharge:.2f}")

print(f"Total Electricity Bill: ₹{bill:.2f}")
