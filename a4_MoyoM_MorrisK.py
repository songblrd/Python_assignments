# Project: Assignment 4
# Purpose:
# Revision History:
#    Date created: 11/18/2024 by Marianne Moyo
#         Additions made on 12/2/2024


class Players:
    def __init__(self, name, position, points):
        self.name = name
        self.position = position
        self.__private_points = points

    def display_player(self):
        print(f"Player information: \n Name: {self.name} \n Position: {self.position} \n Points: {self.__private_points}")

    @staticmethod
    def player_track():
        tracking = Tracker()
        return print(f"Number of players: {tracking.id}")

    @staticmethod
    def team_name():
        return print("Conestoga Condors")

    def update_points(self, new_points):
         self.__private_points = new_points

class Tracker:
    id = 0

    def __init__(self):
        Tracker.id += 1
        self.id = Tracker.id

def main_menu():
    while True:
        print("Main Menu")
        print("1. Add Player")
        print("2. Edit Points")
        print("3. Display All Players")
        print("4. Exit")
        try:
            menu_selection = int(input("Enter a Number: "))
        except ValueError:
            print("Please choose a number.")
            main_menu()

        if menu_selection == 1:
            add_player()
        elif menu_selection == 2:
            edit_points()
        elif menu_selection == 3:
            display_players_all()
        elif menu_selection == 4:
            print("Bye Bye")
            exit()
        else:
            print("Please choose a number.")

def add_player():
    name_input = input("Enter the player's name: ")
    position_input = input("Enter the player's position: ")
    points_input = int(input("Enter the player's points: "))
    p2 = Players(name_input, position_input, points_input)
    players_list.append(p2)
    p2.display_player()
    p2.player_track()
    print("Player added")

def edit_points():
    try:
     find_player = input("Enter the player's name to edit points: ")
    except ValueError:
        print("Enter in the player name.")
        main_menu()
    except UnboundLocalError:
        print("Enter in the player name.")
        main_menu()
    for player in players_list:
        if player.name == find_player:
            try:
             new_points = int(input(f"Enter in a number with no negative sign for {player.name}: "))
            except ValueError:
                print("Enter in a number with no negative sign in front.")
                edit_points()
            try:
             if new_points < 0:
                print("Points inputted cannot have a negative sign in front.")
                edit_points()
             else:
              player.update_points(new_points)
              print(f"Updated points for {player.name}.")
              main_menu()
            except UnboundLocalError:
                print("Enter in the player name.")
                edit_points()

        else:
         print("Player not found.")

# Keegan helped me with this part and I edited it to display the team name
def display_players_all():
    for player in players_list:
        player.team_name()
        player.display_player()
        player.player_track()
        print()

players_list = []

# Adding a player for demonstration
p1 = Players("Bob", "forward", 15)
players_list.append(p1)

main_menu()