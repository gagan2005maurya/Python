# Total theater capacity and currently available seats
total_seats = 100
booked_seats = 40
available_seats = total_seats - booked_seats

print(f"Currently available seats: {available_seats}")

tickets_requested = int(
    input("Enter the number of tickets you want to book: ")
)

if tickets_requested <= available_seats:
  print("Seats are available!")
  print(f"Successfully booked {tickets_requested} tickets. Enjoy your movie!")
else:
  print(
      "Booking failed: Requested number of seats exceeds available seats or is"
      " invalid."
  )
  