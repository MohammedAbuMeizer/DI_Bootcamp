from game import Game

def get_user_menu_choice():
    play_choice = input("\nyour choice is : ")
    return play_choice
    
#input("Select (r)ock , (p)aper, (s)cissors : ")      
def print_results(results):
    print("Game result\n")
    for item , value  in results.items():
        print(f"          You {item} {value} times")
    print("\nThank you for playing")

def main():
    dic = {"win" : 0 , "loss" : 0 ,"draw":0}
    found = True
    while found:
        print("\nMenu : ")
        print("(g) play a new game.")
        print("(x) Show scores and exit.")
        choice = get_user_menu_choice()
        if choice == "g":
            game = Game()
            re = game.play()
            re = f"{re}"
            dic[re] += 1
            found = True
        elif choice == "x":
            print_results(dic)
            found = False
        else :
            print("Menu : ")
            print("(g) play a new game.")
            print("(x) Show scores and exit.")
            choice = get_user_menu_choice()

main()