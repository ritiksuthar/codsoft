import random
list = ["r", "p","s"] 

user_score = 0
computer_score = 0
while True:
    print("----------------------------------START GAME----------------------------------")
    print("\n--->r for rock \n--->p for paper \n--->s for  scissors ")
        
    computer_choice = random.choice(list)
    user_choice = input("Enter your choice: ")
  
    if computer_choice == user_choice:
        print(f"computer choice is  {computer_choice} and your choice is {user_choice} ")
        print("try..again..!\n")
     
        
    elif computer_choice == "r" and user_choice == "p":
        print("computer choice is  ROCK and your choice is PAPER ")
        print("You are Win....") 
        user_score +=1     
    elif computer_choice == "r" and user_choice == "s":
        print("computer choice is  ROCK and your choice is SCISSORS ")
        print("You are Loose....")
        computer_score +=1    
    elif computer_choice == "p" and user_choice == "r":
        print("computer choice is  PAPER and your choice is ROCK ")
        print("You are Loose....")
        computer_score +=1    
    elif computer_choice == "p" and user_choice == "s":
        print("computer choice is  PAPER and your choice is SCISSORS ")
        print("You are Win....")
        user_score +=1    
    elif computer_choice == "s" and user_choice == "r":
        print("computer choice is  SCISSORS and your choice is ROCK ")
        print("You are Win....")
        user_score +=1    
    elif computer_choice == "s" and user_choice == "p":
        print("computer choice is SCISSORS and your choice is PAPER ")
        print("You are Loose....")
        computer_score +=1
    else:
        print("wrong choice...")
    
    print("\n")

    score_board = print(f"USER SCORE IS {user_score} AND COMPUTER SCORE IS {computer_score}")
    play_again = input("Are you Exit in this game...(y/n):")
    if play_again == "y" or play_again =='Y':
        break        
            
print("----------------------------------GAME OVER----------------------------------")