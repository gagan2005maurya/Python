age = int(input("Enter your age: "))

if age >= 18:  #[span_17](start_span)[span_17](end_span)
  has_learner = (
      input("Do you have a learner license? (yes/no): ").strip().lower()
  )
  if has_learner == "yes":  # Check whether a learner license is available[span_18](start_span)[span_18](end_span)
    test_score = float(input("Enter your driving test score: "))
    if test_score >= 60:  #[span_19](start_span)[span_19](end_span)
      print("Driving License Approved!")
    else:
      print("Driving License Rejected: Driving test score is below 60.")
  else:
    print("Driving License Rejected: Learner license is required.")
else:
  print("Driving License Rejected: Age must be at least 18.")
  