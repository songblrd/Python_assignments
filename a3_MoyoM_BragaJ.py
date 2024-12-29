# Project ID: Assignment #3 for Prog1925
# Purpose: Concert Reservation System
# Revision history: Date created 11/01/2024 by Marianne Moyo



# Functions
def new_reservation(list_1):
    row_name2 = 0
    row_name1 = 0
    for element in list_1:
        row_name1 += 1
        print(f"Row {row_name1}: {element}")
    try:
       desired_row = int(input("Enter which row you would like: "))
       desired_seat = int(input("Enter which seat you would like: "))
       reservation_name = str(input("Please enter your name: "))
       list_1[desired_row-1][desired_seat-1] = reservation_name
    except TypeError:
        print("Something went wrong")
    except IndexError:
        print("There was trouble reserving the seat")
    except ValueError:
        print(f"Enter in a number between 1 and {row}.")

    for element in list_1:
        row_name2 += 1
        print(f"Row {row_name2}: {element}")


def edit_reservation(list_1):
    row_name2 = 0
    for element in list_1:
        row_name2 += 1
        print(f"Row {row_name2}: {element}")
    try:
        reserved_row = int(input("Enter which row your seat is reserved: "))
        reserved_seat = int(input("Enter which seat you have reserved: "))
        name = str(input("Enter Reservation Name: "))
        if name == '' or " ":
           new_name = input("Enter new reservation name: ")
           list_1[reserved_row-1][reserved_seat-1] = new_name
           print("Reservation changed.")
           for element in list_1:
               row_name2 = 0
               row_name2 += 1
               print(f"Row {row_name2}: {element}")
        else:
            print("Seat is not reserved")
    except TypeError:
        print("Something went wrong.")
    except ValueError:
        print("Invalid Name")

def cancel_reservation(list_1):
    row_name2 = 0
    for element in list_1:
        row_name2 += 1
        print(f"Row {row_name2}: {element}")
    try:
        cancel_row = int(input("Enter the reserved seat's row for cancellation: "))
        cancel_seat = int(input("Enter which seat you would like to cancel: "))
        cancel = input("Would you like to cancel your reservation? Y/N: ")
        if cancel == "Y":
            list_1[cancel_row-1][cancel_seat-1] = cancel_seat
            row_name2 = 0
            for element in list_1:
                row_name2 += 1
                print(f"Row {row_name2}: {element}")
            print("Reservation Cancelled.")
        else:
            main_menu
    except ValueError:
        print("Something went wrong")




concert_seats = []
row_name = 0
col = 0
row = 0
while row == 0 or col == 0:
 try :
  col = int(input("Enter how many rows: "))
  row = int(input("Enter how many seats per row: "))
 except ValueError:
    print("Enter a number.")

#using list to create empty list
seats = list()
for i in range(1, row + 1):
    seats.append(i)

# testing different solutions
list_1 = []
for j in range(1, col + 1):
    list_2 = []
    for i in range(1, row + 1):
        list_2.append(i)
    list_1.append(list_2)

# Row names
for element in list_1:
    row_name += 1
    print(f"Row {row_name}: {element}")


main_menu = True
try:
   while main_menu:
    print("Main Menu")
    print("\n")
    print("1. Add New Reservation")
    print("2. Edit Existing Reservation")
    print("3. Cancel Reservation")
    print("4. Display Seating Chart")
    print("5. Exit")
    choice = int(input("\nSelect an option: "))

    if choice == 1:
        new_reservation(list_1)
    elif choice == 2:
        edit_reservation(list_1)
    elif choice == 3:
        cancel_reservation(list_1)
    elif choice == 4:
        row_name2 = 0
        for element in list_1:
            row_name2 += 1
            print(f"Row {row_name2}: {element}")
    elif choice == 5:
        main_menu = False
    else:
       print()
except ValueError:
    print("Enter an option.")

