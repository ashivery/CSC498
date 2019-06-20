from random import randint

def PlayGame():
    print('Welcome to rock-paper-scissors !\n')
    GameRecord = [[],[],[]]
    
    while True:
        ChoiceOfHumanPlayer = HumanPlayer(GameRecord)
        if (ChoiceOfHumanPlayer == 'quit'):
            break
        ChoiceOfComputerPlayer = ComputerPlayer(GameRecord)
        Outcome = Judge(ChoiceOfComputerPlayer, ChoiceOfHumanPlayer)
        PrintOutcome(Outcome, ChoiceOfComputerPlayer, ChoiceOfHumanPlayer)
        UpdateGameRecord(GameRecord, ChoiceOfComputerPlayer, ChoiceOfHumanPlayer, Outcome)
        
    print('\n-------Game Over-------')
        

def HumanPlayer(GameRecord):
    loopOne = 1
    ChoiceOfHumanPlayer = ""
    
    while (loopOne != 0):
        print("let's play .................")
        print("rock(r), paper(p), scissors(s))?\nor you want to see a record of the game(g)?")
        print("or you want to quit(q)\nplease make your choice now: ")
        choice = input()
        
        if (choice == 'r' or choice == 'rock'):
            ChoiceOfHumanPlayer = 'rock'
            loopOne = 0
        elif (choice == 'p' or choice == 'paper'):
            ChoiceOfHumanPlayer = 'paper'
            loopOne = 0
        elif (choice == 's' or choice == 'scissors'):
            ChoiceOfHumanPlayer = 'scissors'
            loopOne = 0
        elif (choice == 'g' or choice == 'game'):
            PrintGameRecord(GameRecord)
        elif (choice == 'q' or choice == 'quit'):
            ChoiceOfHumanPlayer = 'quit'
            loopOne = 0
        else:
            print("\nInvalid input, please try again.\n")
            
    return ChoiceOfHumanPlayer

def ComputerPlayer(GameRecord):
    compRand = randint(1,3)
    
    if compRand == 1:
        ChoiceOfComputerPlayer = 'rock'
    if compRand == 2:
        ChoiceOfComputerPlayer = 'paper'
    if compRand == 3:
        ChoiceOfComputerPlayer = 'scissors'
    
    return ChoiceOfComputerPlayer

def Judge(ChoiceOfComputerPlayer, ChoiceOfHumanPlayer):
    if ChoiceOfComputerPlayer == ChoiceOfHumanPlayer:
        Outcome = 0
    elif (ChoiceOfComputerPlayer == 'rock' and ChoiceOfHumanPlayer == 'scissors'):
        Outcome = 1
    elif (ChoiceOfComputerPlayer == 'paper' and ChoiceOfHumanPlayer == 'rock'):
        Outcome = 1
    elif (ChoiceOfComputerPlayer == 'scissors' and ChoiceOfHumanPlayer == 'paper'):
        Outcome = 1
    else:
        Outcome = 2

    return Outcome
        
def UpdateGameRecord(GameRecord, ChoiceOfComputerPlayer, ChoiceOfHumanPlayer, Outcome):
    GameRecord[0].append(ChoiceOfHumanPlayer)
    GameRecord[1].append(ChoiceOfComputerPlayer)
    GameRecord[2].append(Outcome)
    
def PrintOutcome(Outcome, ChoiceOfComputerPlayer, ChoiceOfHumanPlayer):
    print('\n-------Outcome-------\n')
    if (Outcome == 0):
        print('It is a tie: Computer chose %s ; Human chose %s' % (ChoiceOfComputerPlayer, ChoiceOfHumanPlayer))
    elif(Outcome == 1):
        print('Computer wins: Computer chose %s ; Human chose %s' % (ChoiceOfComputerPlayer, ChoiceOfHumanPlayer))
    elif(Outcome == 2):
        print('Human wins: Computer chose %s ; Human chose %s' % (ChoiceOfComputerPlayer, ChoiceOfHumanPlayer))
    print("\n---------------------\n")

def PrintGameRecord(GameRecord):
    Cwins = 0
    Hwins = 0
    rounds = 0
    for i in GameRecord[2]:
        if i == 1:
            Cwins += 1
        if i == 2:
            Hwins += 1
        rounds += 1
    print('\n-------Record Of The Game-------\n')
    print('The number of rounds is %d' % rounds)
    print("Human wins", Hwins, "round(s)")
    print("Computer wins", Cwins, "round(s)")
    print("Human, Computer")
    x = 0
    while x < len(GameRecord[2]):
        print(GameRecord[0][x], ",", GameRecord[1][x])
        x += 1
    print("\n--------------------------------\n")
    
PlayGame()

        
