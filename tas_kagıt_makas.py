choice1=input("What is first player's choice: ")
choice2=input("What is second player's choice: ")
rock="1"
paper="2"
scissors="3"

while True:
    if choice1==rock and choice2==paper:
     print("Second player won.")
     break
    elif choice1==rock and choice2==scissors:
     print("First player won.")
     break
    elif choice1==scissors and choice2==rock:
     print("Second player won.")
     break
    elif choice1==scissors and choice2==paper:
     print("First player won.")
     break
    elif choice1==paper and choice2==rock:
     print("First player won.")
     break
    elif choice1==paper and choice2==scissors:
     print("Second player won.")
     break
    else:
        print("Game is even-steven")
        break
        
        
    