employees = {
    "Rahul": {"salary": 60000, "department": "IT"},
    "Amit": {"salary": 40000, "department": "HR"},
    "Priya": {"salary": 70000, "department": "IT"},
    "Neha": {"salary": 45000, "department": "Finance"}
}

for name, info in employees.items():
    salary = info["salary"]
    department = info["department"]
    
    if salary >= 50000:
        if department == "IT":
            category = "Senior IT Employee"
        elif department == "HR":
            category = "Senior HR Employee"
        else:
            category = "Senior Employee"
    else:
        category = "Junior Employee"
        
    print(f"{name}: {category}")
    