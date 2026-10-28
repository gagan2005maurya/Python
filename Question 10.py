even_count = 0
odd_count = 0
for i in range(1, 51):
  if i % 2 == 0:
    even_count += 1
  else:
    odd_count += 1

print(f"Number of even numbers: {even_count}")
print(f"Number of odd numbers: {odd_count}")
