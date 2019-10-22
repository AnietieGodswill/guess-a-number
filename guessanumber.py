import random
randomVal = random.randint(0, 100)
noOFguesses = 1
print("((GUESS A NUMBER)) "
      "Created By - Nishant Tiwari")
print("Try to guess a number from (0 to 100)")
while(noOFguesses<=10):
    guessNum = int(input("Enter a number"))

    if(guessNum <randomVal):
        print("You enter a smaller no.,input a greater no.")

    elif(guessNum >randomVal):
        print("You enter a greater no.,input a smaller no. ")
    
    else:
        print("Congratulations, you won!!!")
        break

    print(10 - noOFguesses, "No. of guess left")
    noOFguesses = noOFguesses + 1
    if (noOFguesses >10):
        print("Game Over!!!")
