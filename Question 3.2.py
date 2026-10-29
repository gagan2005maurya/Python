# Student performance evaluation using nested if conditions[span_2](start_span)[span_2](end_span)
students = {
    "Rahul": 85,
    "Amit": 35,
    "Priya": 72,
    "Neha": 48
}

for name, marks in students.items():
    if marks >= 40:
        if marks >= 60:
            if marks >= 80:
                category = "Excellent" # Marks >= 80[span_4](start_span)[span_4](end_span)
            else:
                category = "Good" # Marks >= 60 and < 80[span_5](start_span)[span_5](end_span)
        else:
            category = "Average" # Marks >= 40 and < 60[span_6](start_span)[span_6](end_span)
    else:
        category = "Fail" # Marks < 40[span_7](start_span)[span_7](end_span)
    print(f"{name}: {category}")
    