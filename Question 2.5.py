# Predefined credentials for validation
correct_username = "admin123"
correct_password = "mypassword"

username = input("Enter username: ")

if username == correct_username:
  password = input("Enter password: ")
  if password == correct_password:
    role = input("Enter role (admin/teacher/student): ").strip().lower()
    if role == "admin":
      print("Full Access")
    elif role == "teacher":
      print("Teacher Dashboard")
    elif role == "student":
      print("Student Dashboard")
    else:
      print("Invalid Role")
  else:
    print("Wrong Password")
else:
  print("Invalid Username")
  