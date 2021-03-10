import random
class Game():
    def get_user_item(self):
        found = True
        choice = input("Select (r)ock , (p)aper, (s)cissors : ")
        while found:
            if choice == "r"  :
                found = False
                return choice
            elif choice == "p":
                found = False
                return choice
            elif choice == "s":
                found = False
                return choice
            else :
                choice = input("Select (r)ock , (p)aper, (s)cissors : ")
    
    def get_computer_item(self):
        list_choices = ["r","p","s"]
        computer_choise = random.choice(list_choices)
        return computer_choise 
    
    def get_game_result(self, user_item, computer_item):
        result = ""
        if user_item == computer_item:
            result = "draw"
            return result
        elif user_item == "r" and computer_item == "p":
            result = "loss"
            return result
        elif user_item == "r" and computer_item == "s":
            result = "win"
            return result
        elif user_item == "p" and computer_item == "r":
            result = "win"
            return result
        elif user_item == "p" and computer_item == "s":
            result = "loss"
            return result
        elif user_item == "s" and computer_item == "r":
            result = "loss"
            return result
        elif user_item == "s" and computer_item == "p":
            result = "win"
            return result
        

#
    def play(self):
        user = self.get_user_item()
        com = self.get_computer_item()
        result = self.get_game_result(user,com)
        print(f"You selected {user} .The computer selected {com} .\nYou {result}")
        return result