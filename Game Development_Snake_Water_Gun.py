import random

# print(choies)
# print(lower_case_input)
a = 10

# # while (a > 0):
#     user_input_game = input("Chose Snake ,Water or Gun\n")
#     lower_case_input = user_input_game.lower()
#     a = a-1
#     Cscore = 0
#     user_Score = 0
#     if choies == "water" and lower_case_input == "s":
#         user_score = user_score + 1
#         print(user_score)
#         a = a-1
#         continue


#     elif choies == "snake" and lower_case_input == "w":
#         Cscore = Cscore + 1
#         a = a-1
#         continue


#     elif choies == "gun" and lower_case_input == "s":
#         Cscore= Cscore +1
#         a= a-1
#         continue


# try:
#     while True:
#         inp = int(input("enter\n"))
#         if inp==2:
#             break
#         else:
#             continue
# except Exception as error:
#     print("error")

print("Game Development: Snake Water Gun")
game_cher = ["water", "snake", "gun"]
choies_Computer = random.choice(game_cher)


def game_function(computer):
    time_run_while_loop = 10
    computer_score = 0
    user_score = 0
    while time_run_while_loop > 0:
        chose_user = input("Chose 'S' For Snake 'G' For Gun 'W' For Water\n")


        #user Win game
        if computer == "water" and chose_user == "s":
            user_score = user_score + 1
            print("Your Score is ", user_score)
            time_run_while_loop = time_run_while_loop - 1


        elif computer=="gun" and chose_user=="w":
            user_score = user_score + 1
            print("Your Score is ", user_score)
            time_run_while_loop = time_run_while_loop -1


        elif computer == "snake" and chose_user == "g":
            user_score = user_score + 1
            print("Your Score is ", user_score)
            time_run_while_loop = time_run_while_loop -1




        #Computer Win game
        elif computer == "snake" and chose_user == "w":
            computer_score = computer_score +1
            print("computer Score is " , computer_score)
            time_run_while_loop = time_run_while_loop -1

        elif computer == "gun" and chose_user =="s":
            computer_score = computer_score +1
            print("computer Score is " , computer_score)
            time_run_while_loop = time_run_while_loop -1

        elif computer == "water" and chose_user == "g":
            computer_score += 1
            print("computer Score is " , computer_score)
            time_run_while_loop -= 1
       





        #draw game
        elif computer == "water" and chose_user == "w":
            time_run_while_loop -=1
            print("Draw Game Score")
 
        elif computer =="snake" and chose_user == "s":
            time_run_while_loop -= 1
            print("Draw Game Score")

        elif computer == "gun" and chose_user == "g":
            time_run_while_loop -= 1
            print("Draw Game Score")
        else:
          print("Enter Valid key")

    



    #winer Check
    print("your Score is " , user_score)
    print("computer Score " ,computer_score)
    if user_score > computer_score:
        print("you Win")

    elif user_score==computer_score:
        print("Draw Game")
    
    else:
      print("You Lose")

    replay = input("do you play again y/n \n")
    if replay == "y":
        game_function(choies_Computer)

    
       
      


game_function(choies_Computer)
