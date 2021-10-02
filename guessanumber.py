import random
randomVal = random.randint(0, 100)
noOFguesses = 1
print("((GUESS A NUMBER))"
      "Created By - Nishant Tiwari")
print("Try To Guess A Number from (0 to 100)")
while(noOFguesses<=10):
    guessNum = int(input("Enter A Number"))

    if(guessNum <randomVal):
        print("You Enter A Smaller Number.,Enter A Greater Number.")

    elif(guessNum >randomVal):
        print("You enter a greater no.,input a smaller no. ")
    
    else:
        print("Congratulations, you won!!!")
        break

    print(10 - noOFguesses, "No. of guess left")
    noOFguesses = noOFguesses + 1
    if (noOFguesses >10):
        print("Game Is Over!!")
