class Star_Cinema:
    hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls.hall_list.append(hall)


class Hall:
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no

        Star_Cinema.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self._show_list.append(show_info)
        seats = [['FREE' for _ in range(self._cols)] for _ in range(self._rows)]
        self._seats[id] = seats

    def book_seats(self, id, seat_list):
        try:
            seats = self._seats[id]
        except KeyError:
            raise ValueError("INVALID SHOW ID. SHOW NOT FOUND.")

        for row, col in seat_list:
            if 1 <= row <= self._rows and 1 <= col <= self._cols:
                if seats[row - 1][col - 1] == 'FREE':
                    seats[row - 1][col - 1] = 'BOOKED'
                else:
                    raise ValueError("SEAT {}-{} IS ALREADY BOOKED.".format(row, col))
            else:
                raise ValueError("INVALID SEAT NUMBER: {}-{}".format(row, col))

    def view_show_list(self):
        return self._show_list

    def view_available_seats(self, id):
        try:
            seats = self._seats[id]
        except KeyError:
            raise ValueError("INVALID SHOW ID. SHOW NOT FOUND.")

        available_seats = []
        for row in range(1, self._rows + 1):
            for col in range(1, self._cols + 1):
                if seats[row - 1][col - 1] == 'FREE':
                    available_seats.append((row, col))

        return available_seats


def main():
    print("-----------------------")
    print("WELCOME TO STAR CINEMA!")
    print("-----------------------")

    while True:
        print("\n1. CREATE A NEW HALL")
        print("2. ENTER A NEW SHOW")
        print("3. VIEW ALL SHOWS")
        print("4. VIEW AVAILABLE SEATS FOR A SHOW")
        print("5. BOOK SEATS FOR A SHOW")
        print("6. EXIT\n")

        choice = input("ENTER YOUR CHOICE: ")

        if choice == '1':
            rows = int(input("\nENTER THE NUMBER OF ROWS FOR THE NEW HALL: "))
            cols = int(input("ENTER THE NUMBER OF COLUMNS FOR THE NEW HALL: "))
            hall_no = len(Star_Cinema.hall_list) + 1
            hall = Hall(rows, cols, hall_no)
            print("--------------------------")
            print(f"HALL {hall_no} CREATED.")
            print("--------------------------")

        elif choice == '2':
            hall_no = int(input("ENTER THE HALL NUMBER: "))
            id = input("ENTER THE SHOW ID: ")
            movie_name = input("ENTER THE MOVIE NAME: ")
            time = input("ENTER THE SHOW TIME: ")
            for hall in Star_Cinema.hall_list:
                if hall._hall_no == hall_no:
                    hall.entry_show(id, movie_name, time)
                    print("-------------------------------------")
                    print(f"SHOW '{id}' ADDED TO HALL {hall_no}.")
                    print("-------------------------------------")


        elif choice == '3':
            for hall in Star_Cinema.hall_list:
                print(f"HALL {hall._hall_no} SHOWS:")
                for show in hall.view_show_list():
                    print("-------------------------------------------------")
                    print(f"ID: {show[0]}, MOVIE: {show[1]}, TIME: {show[2]}")
                    print("-------------------------------------------------")

        elif choice == '4':
            id = input("ENTER THE SHOW ID: ")
            for hall in Star_Cinema.hall_list:
                if hall._hall_no == hall_no:
                    available_seats = hall.view_available_seats(id)
                    print("---------------------------------------------------")
                    print(f"AVAILABLE SEATS FOR SHOW '{id}': {available_seats}")
                    print("---------------------------------------------------")

        elif choice == '5':
            id = input("ENTER THE SHOW ID: ")
            hall_no = int(input("ENTER THE HALL NUMBER: "))
            try:
                seat_list = eval(input("ENTER SEAT NUMBERS AS A LIST OF TUPLES (E.G., [(1, 2), (3, 4)]): "))
                for hall in Star_Cinema.hall_list:
                    if hall._hall_no == hall_no:
                        hall.book_seats(id, seat_list)
                        print("-------------------------------------------------------------")
                        print(f"SEATS BOOKED SUCCESSFULLY FOR SHOW '{id}' IN HALL {hall_no}.")
                        print("-------------------------------------------------------------")
            except Exception as e:
                print("ERROR:", e)

        elif choice == '6':
            print("--------------------------------")
            print("THANK YOU FOR USING STAR CINEMA!")
            print("--------------------------------")
            break

        else:
            print("---------------------------------")
            print("INVALID CHOICE. PLEASE TRY AGAIN.")
            print("---------------------------------")


if __name__ == "__main__":
    main()