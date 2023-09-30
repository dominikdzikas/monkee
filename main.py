# Write your code here
class Monkee:

    def __init__(self, game_name: str):
        self.game_name = game_name
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
                print("\nGreat, now let's go code some more ;)")
                return False
            elif choice == "no":
                print("\nHow about now.\nAre you ready to begin?\n\t[Yes] [No]")
            elif choice == "menu":
                return True

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
    game = Monkee(gamename)
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
