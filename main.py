# Write your code here
class Monkee:

    def __init__(self, game_name: str, ui: str, ingame_menu_str: str):
        self.game_name = game_name
        self.ui = ui
        self.ingame_menu_str = ingame_menu_str
        self.username = "guest"
        self.menu_options = ["[Play]", "[High] scores", "[Help]", "[Exit]"]

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
                while True:
                    print(self.ui)
                    player_move = self.read_command(["ex", "up", "save", "m"])
                    if player_move == "m":
                        is_bool = self.ingame_menu()
                        if is_bool in [True, False]:
                            return is_bool

                    else:
                        print("Coming SOON!")
                        return False
            elif choice == "no":
                print("\nHow about now.\nAre you ready to begin?\n\t[Yes] [No]")
            elif choice == "menu":
                return True

    def ingame_menu(self):
        print(self.ingame_menu_str)
        while True:
            ingame_choice = self.read_command(["back", "main", "save", "exit"])
            if ingame_choice == "back":
                break
            elif ingame_choice == "main":
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
    gamename = """+===================================================
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
|                  [Ex]plore                          [Up]grade                                  |
|                  [Save]                             [M]enu                                     |
+================================================================================================+"""
    menu = """\n|==========================|
              |            MENU          |
              |                          |
              | [Back] to game           |
              | Return to [Main] Menu    |
              | [Save] and exit          |
              | [Exit] game              |
              |==========================|"""
    game = Monkee(gamename, ui, menu)
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
