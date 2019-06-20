from random import randint


def TicTacToeGame():
    
    print("Welcome to Tic Tac Toe Game\n")
    Board = [[" ", " ", " "],
             [" "," "," "],
             [" "," "," "]]
    
    DrawBoard(Board)
    
    goesFirst = randint(1,2)
    
    #HUMAN GOES FIRST
    if goesFirst == 1:
        print("\nHuman Player goes first.\nMake your choice")
        Tag = 'X'
        while True:
            while True:
                ChoiceOfHumanPlayer = HumanPlayer(Tag, Board)
                isFree = IsSpaceFree(ChoiceOfHumanPlayer, Board)
                if isFree != 0: 
                    print("Space is taken, try again")
                else:
                    UpdateBoard(ChoiceOfHumanPlayer, Board, Tag)
                    break
            
            print("\nHuman Player(X) has made the choice\n")
            DrawBoard(Board)
            Outcome = Judge(Board)
            ShowOutcome(Outcome)
            
            if Outcome == 1 or Outcome == 2 or Outcome == 3:
                break
            
            TagTwo= "O"
            while True:
                ChoiceOfComputerPlayer = ComputerPlayer(TagTwo, Board)
                isFree = IsSpaceFree(ChoiceOfComputerPlayer, Board)
                if isFree == 0: 
                    UpdateBoard(ChoiceOfComputerPlayer, Board, TagTwo)
                    break
            
            print("Computer Player(O) has made the choice\n")
            DrawBoard(Board)
            Outcome = Judge(Board)
            ShowOutcome(Outcome)
            
            if Outcome == 1 or Outcome == 2 or Outcome == 3:
                break
            
    #COMPUTER IS FIRST
    if goesFirst == 2:
        print("\nComputer Player goes first.\n")
        Tag = 'X'
        while True:
            while True:
                ChoiceOfComputerPlayer = ComputerPlayer(Tag, Board)
                isFree = IsSpaceFree(ChoiceOfComputerPlayer, Board)
                if isFree == 0: 
                    UpdateBoard(ChoiceOfComputerPlayer, Board, Tag)
                    break
            print("Computer Player(X) has made the choice\n")
            DrawBoard(Board) 
            Outcome = Judge(Board)
            ShowOutcome(Outcome)
            
            if Outcome == 1 or Outcome == 2 or Outcome == 3:
                break
            
            TagTwo= "O"
            print("\nMake Your Choice")
            while True:
                ChoiceOfHumanPlayer = HumanPlayer(TagTwo, Board)
                isFree = IsSpaceFree(ChoiceOfHumanPlayer, Board)
                if isFree != 0: 
                    print("Space is taken, try again\n")
                else:
                    UpdateBoard(ChoiceOfHumanPlayer, Board, TagTwo)
                    break
            
            print("\nHuman Player(O) has made the choice")
            DrawBoard(Board) 
            Outcome = Judge(Board)
            ShowOutcome(Outcome)
            
            if Outcome == 1 or Outcome == 2 or Outcome == 3:
                break

def HumanPlayer(Tag, Board):  
    while True:
        row = input("row = ")
        if (row == "1") or (row == "2") or (row == "3"):
            break
        else:
            print("Oops, that is not a valid number, try again")
    
    while True:
        col = input("col = ")
        if (col == "1") or (col == "2") or (col == "3"):
            break
        else:
            print("\nOops, that is not a valid number, try again")  
    intRow = int(row)
    intCol = int(col)
    intRow -= 1
    intCol -= 1
    
    ChoiceOfHumanPlayer = (intRow, intCol)
    
    return ChoiceOfHumanPlayer

def ComputerPlayer(Tag, Board):
    compRand = randint(0,2)
    compRow = compRand
    compRand1 = randint(0,2)
    compColumn = compRand1
    ChoiceOfComputerPlayer = (compRow, compColumn)
    
    return ChoiceOfComputerPlayer            
    
def DrawBoard(Board):
    print(Board[0][0] + " | " + Board [0][1] + " | " + Board[0][2])
    print("---------")
    print(Board[1][0] + " | " + Board [1][1] + " | " + Board[1][2]) 
    print("---------")
    print(Board[2][0] + " | " + Board [2][1] + " | " + Board[2][2])
    
def UpdateBoard(ChoiceOfPlayer, Board, Tag):
        Board[ChoiceOfPlayer[0]][ChoiceOfPlayer[1]] = Tag

def IsSpaceFree(ChoiceOfPlayer, Board):
    if (Board[ChoiceOfPlayer[0]][ChoiceOfPlayer[1]] == " "):
        return 0
    else:
        return 1

def Judge(Board):
    #If X Wins
    if Board[0][0] == Board[1][1] == Board[2][2] == 'X': #DiagLeftToRight
        Outcome = 1
        return Outcome
    elif Board[0][0] == Board[0][1] == Board[0][2] == 'X': #AcrossTop
        Outcome = 1
        return Outcome
    elif Board[0][0] == Board[1][0] == Board[2][0] == 'X': #DownLeft
        Outcome = 1
        return Outcome
    elif Board[0][1] == Board[1][1] == Board[2][1] == 'X': #DownMiddle
        Outcome = 1
        return Outcome
    elif Board[0][2] == Board[1][2] == Board[2][2] == 'X': #DownRight
        Outcome = 1
        return Outcome
    elif Board[1][0] == Board[1][1] == Board[1][2] == 'X': #AcrossMiddle
        Outcome = 1
        return Outcome
    elif Board[2][0] == Board[2][1] == Board[2][2] == 'X': #Across Bottom
        Outcome = 1
        return Outcome
    elif Board[2][0] == Board[1][1] == Board[0][2] == 'X': #DiagBotleftToTopRight
        Outcome = 1
        return Outcome
    
    #If O Wins
    elif Board[0][0] == Board[1][1] == Board[2][2] == 'O': #DiagLeftToRight
        Outcome = 2
        return Outcome
    elif Board[0][0] == Board[0][1] == Board[0][2] == 'O': #AcrossTop
        Outcome = 2
        return Outcome
    elif Board[0][0] == Board[1][0] == Board[2][0] == 'O': #DownLeft
        Outcome = 2
        return Outcome
    elif Board[0][1] == Board[1][1] == Board[2][1] == 'O': #DownMiddle
        Outcome = 2
        return Outcome
    elif Board[0][2] == Board[1][2] == Board[2][2] == 'O': #DownRight
        Outcome = 2
        return Outcome
    elif Board[1][0] == Board[1][1] == Board[1][2] == 'O': #AcrossMiddle
        Outcome = 2
        return Outcome
    elif Board[2][0] == Board[2][1] == Board[2][2] == 'O': #Across Bottom
        Outcome = 2
        return Outcome
    elif Board[2][0] == Board[1][1] == Board[0][2] == 'O': #DiagBotleftToTopRight
        Outcome = 2
        return Outcome
    
    counter = IsBoardFull(Board)
    
    if counter == 9:
        Outcome = 3    
        return Outcome
    
    counter = GetNumberOfChessPieces(Board)
    
    if counter >0 and counter < 9:
        Outcome = 0
        return Outcome

def IsBoardFull(Board):
    counter = 0
    for i in range(len(Board)):
        for j in range(len(Board[i])):
            if (Board[i][j] == "X") or Board[i][j] == "O":
                counter += 1
    return counter

def GetNumberOfChessPieces(Board):
    counter = 0
    for i in range(len(Board)):
        for j in range(len(Board[i])):
            if (Board[i][j] == " "):
                counter += 1
    return counter

def ShowOutcome(Outcome):
    if Outcome == 1:
        print("\nPlayer X Wins!")
    if Outcome == 2:
        print("\nPlayer O Wins!")
    if Outcome == 3:
        print("\nGame ends in a tie")
    if Outcome == 0:
        print("\nGame still in progress\n")

def PlayGame():
    while True:
        TicTacToeGame()
        print("\nDo you want to play again(enter y or n)")
        if not input().lower().startswith('y'):
            break
    print("\nGame Over")
    
PlayGame()
