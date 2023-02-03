class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    # add passenger to a flightusing self (the object itself)
    def add_passenger(self, name):
        if not self.open_seats():    # saying same as if
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)


flight = Flight(3)

people = ['carla', 'rodolfo', 'victoria', 'jose']
# more explicit
# for person in people:
#     success = flight.add_passenger(person)
#     if success:
#         print(f'Added {person} to flight successfully.')
#     else:
#         print(f'No available seats for {person}')

# more resumed
for person in people:
    # removing the variable and directly checking if true or false
    if flight.add_passenger(person):
        print(f'Added {person} to flight successfully.')
    else:
        print(f'No available seats for {person}')
