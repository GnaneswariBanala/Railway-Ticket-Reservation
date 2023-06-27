class Train:
    def __init__(self, train_number, train_name, available_seats):
        self.train_number = train_number
        self.train_name = train_name
        self.available_seats = available_seats

    def reserve_ticket(self, num_tickets):
        if num_tickets <= self.available_seats:
            self.available_seats -= num_tickets
            print(f"{num_tickets} ticket(s) reserved for Train {self.train_number} - {self.train_name}")
            print(f"Available seats: {self.available_seats}")
        else:
            print("Insufficient seats available.")

    def display_available_seats(self):
        print(f"Available seats for Train {self.train_number} - {self.train_name}: {self.available_seats}")


def main():
    # Create Train objects
    train1 = Train("T001", "Express", 100)
    train2 = Train("T002", "Local", 50)

    # Perform ticket reservation
    train1.display_available_seats()
    train1.reserve_ticket(3)
    train1.display_available_seats()

    train2.display_available_seats()
    train2.reserve_ticket(2)
    train2.display_available_seats()


if __name__ == "__main__":
    main()
