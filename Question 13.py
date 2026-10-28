data = [22, 55, 12, 89, 34, 67]
smallest = data[0]
for num in data:
  if num < smallest:
    smallest = num

print("The smallest number is:", smallest)
