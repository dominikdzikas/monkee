# Write your code here
import argparse
import random

parser = argparse.ArgumentParser("Not yet")
parser.add_argument("seed")
parser.add_argument("min_duration")
parser.add_argument("max_duration")
parser.add_argument("locations")
args = parser.parse_args()


class Monkee:

    def __init__(self, game_name: str, ui: str, ingame_menu_str: str, args: parser.parse_args()):
        self.game_name = game_name
        self.ui = ui
        self.ingame_menu_str = ingame_menu_str
        self.username = "guest"
        self.menu_options = ["[Play]", "[High] scores", "[Help]", "[Exit]"]
        self.args = args

    def start_menu(self):
        print(self.game_name)
        print(*self.menu_options, sep="\n")
        return self.read_command(["high", "play", "help", "exit"])

    def read_command(self, commands):
        while True:
            print("\nYour command")
            command = input().lower()
            if command in commands:
                return command
            print("Invalid input")

    def play(self):
        self.username = input("\nEnter your name:")
        print(f"Greetings, commander {self.username}!\nAre you ready to begin?\n[Yes] [No] Return to Main[Menu]")
        while True:
            choice = self.read_command(["yes", "no", "menu"])
            if choice == "yes":
                if self.start_game():
                    return True
                print(f"Greetings, commander {self.username}!\nAre you ready to begin?\n[Yes] [No] Return to Main[Menu]")
            elif choice == "no":
                print("\nHow about now.\nAre you ready to begin?\n\t[Yes] [No]")
            elif choice == "menu":
                return True

    def start_game(self):
        all_titanium = 0
        while True:
            print(self.ui)
            player_move = self.read_command(["ex", "up", "save", "m"])
            random.seed(self.args.seed)
            if player_move == "ex":
                new_titanium = self.explore()
                print(new_titanium)
                all_titanium += new_titanium
                print(all_titanium)
            elif player_move == "up":
                break
            elif player_move == "save":
                print("Coming SOON!")
                break
            elif player_move == "m":
                if self.ingame_menu():
                    return True

    def explore(self):
        current_locations = {}
        location_counter = 0
        random.seed(int(self.args.seed))
        current_locations[str(location_counter+1)] = random.choice(self.args.locations.split(","))
        while location_counter < 9:
            [print(key, value) for key, value in current_locations.items()]
            explore_command = self.read_command(["s", "back",  *current_locations.keys()])
            if explore_command == "s":
                location_counter += 1
                current_locations[str(location_counter+1)] = random.choice(self.args.locations.split(","))

            elif explore_command == "back":
                return 0
            else:
                print(current_locations[explore_command])
                return random.randint(10,100)

    def ingame_menu(self):
        print(self.ingame_menu_str)
        while True:
            ingame_choice = self.read_command(["back", "main", "save", "exit"])
            if ingame_choice == "back":
                self.start_game()
            elif ingame_choice == "main":
                return False
            elif ingame_choice == "exit":
                return True
            else:
                print("Coming SOON!")
                return False

    def high_scores(self):
        print("\nNo scores to display.\n\t[Back]")
        self.read_command(["back"])
        return True

    def help(self):
        print("Coming SOON! Thanks for playing!")
        return False

    def exit(self):
        print("Thanks for playing, bye!")
        return False


def main():
    title = """+===================================================
███╗░░░███╗░█████╗░███╗░░██╗██╗░░██╗███████╗███████╗
████╗░████║██╔══██╗████╗░██║██║░██╔╝██╔════╝██╔════╝
██╔████╔██║██║░░██║██╔██╗██║█████═╝░█████╗░░█████╗░░
██║╚██╔╝██║██║░░██║██║╚████║██╔═██╗░██╔══╝░░██╔══╝░░
██║░╚═╝░██║╚█████╔╝██║░╚███║██║░╚██╗███████╗███████╗
╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝╚══════╝
+==================================================="""

    ui = """\n+================================================================================================+                     
         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓         |        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓          |       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓
       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓       |      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓        |     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
     ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓     |    ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓      |   ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓
 ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░ | ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░ | ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░
 ░░░░▓▓░░  ██░░░░░░  ██░░▓▓░░░░ | ░░░░▓▓░░  ██░░░░░░  ██░░▓▓░░░░ | ░░░░▓▓░░  ██░░░░░░  ██░░▓▓░░░░
   ░░▓▓░░████░░░░░░████░░▓▓░░   |   ░░▓▓░░████░░░░░░████░░▓▓░░   |   ░░▓▓░░████░░░░░░████░░▓▓░░
     ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓     |     ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓     |     ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓
       ▓▓░░░░░░░░░░░░░░▓▓       |       ▓▓░░░░░░░░░░░░░░▓▓       |       ▓▓░░░░░░░░░░░░░░▓▓
         ▓▓▓▓░░░░░░▓▓▓▓         |         ▓▓▓▓░░░░░░▓▓▓▓         |         ▓▓▓▓░░░░░░▓▓▓▓
             ▓▓▓▓▓▓        ░░   |             ▓▓▓▓▓▓        ░░   |             ▓▓▓▓▓▓        ░░
           ▓▓▓▓▓▓▓▓▓▓      ▓▓   |           ▓▓▓▓▓▓▓▓▓▓      ▓▓   |           ▓▓▓▓▓▓▓▓▓▓      ▓▓
           ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓   |           ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓   |           ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓
       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓       |       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓       |       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
+================================================================================================+
| Titanium: 0
+================================================================================================+
|                  [Ex]plore                          [Up]grade                                  |
|                  [Save]                             [M]enu                                     |
+================================================================================================+"""
    menu = """              |==========================|
              |            MENU          |
              |                          |
              | [Back] to game           |
              | Return to [Main] Menu    |
              | [Save] and exit          |
              | [Exit] game              |
              |==========================|"""

    game = Monkee(title, ui, menu, args)
    game_status = True
    cases = {
             "play": game.play,
             "high": game.high_scores,
             "help": game.help,
             "exit": game.exit
    }

    while game_status:
        menu_options = game.start_menu()
        game_status = cases[menu_options]()


if __name__ == "__main__":
    main()
