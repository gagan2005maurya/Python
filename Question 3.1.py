students = {
    "Rahul": 75,
    "Amit": 32,
    "Priya": 88,
    "Neha": 39,
    "Rohit": 55,
}  #[span_26](start_span)[span_26](end_span)

for name, marks in students.items():
  if marks >= 40:  # Marks >= 40 -> Pass[span_27](start_span)[span_27](end_span)
    print(f"{name}: {marks} marks -> Pass")
  else:  # Marks < 40 -> Fail[span_28](start_span)[span_28](end_span)
    print(f"{name}: {marks} marks -> Fail")
    