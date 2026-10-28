sub1 = float(input("Enter marks for subject 1: "))
sub2 = float(input("Enter marks for subject 2: "))
sub3 = float(input("Enter marks for subject 3: "))

if sub1 >= 40 and sub2 >= 40 and sub3 >= 40:
  total_marks = sub1 + sub2 + sub3
  percentage = (total_marks / 300) * 100
  print(f"Percentage: {percentage:.2f}%")

  if percentage >= 75:
    print("Distinction")
  elif percentage >= 60:
    print("First Division")
  elif percentage >= 50:
    print("Second Division")
  else:
    print("Pass")
else:
  print("Fail: Marks in one or more subjects are below 40.")
  