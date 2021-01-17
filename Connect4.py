"""
Connect 4 game
Step 1- Draw a 6*7 (r*c matrix)
Example-
 | | | | | | |
 -------------
 | | | | | | |
 -------------
 | | | | | | |
 -------------
 | | | | | | |
 -------------
 | | | | | | |
 -------------
 | | | | | | |
 
"""
def DrawPlayboard(rows,columns):
    if rows <= 23 and columns<=123:
        for row in range(rows+1):
            if row%2==0:
                for column in range(1,columns+1):
                    if column%2==1:
                        if column!=columns:
                            print(" ",end=" ")
                        else:
                            print(" ")
                        print(" ",end="")
                    else:
                        print("|",end="")
            else:
                print('---------------------------')
          
    else:
        return False


        
        
    

def UserInputs():
    Player=1
    currentField=[[" " ," " ," ", " ", " ", " ", " "],[" " ," " ," ", " ", " ", " ", " "],
    [" " ," " ," ", " ", " ", " ", " "],[" " ," " ," ", " ", " ", " ", " "],
    [" " ," " ," ", " ", " ", " ", " "],[" " ," " ," ", " ", " ", " ", " "]]
    
    while(True):
        MoveRow=7
        RowMovement_P1={}
        RowMovement_P2={}
        print("Players Turn", Player)
        MoveColumn= int(input("Enter the column nbr 1-7"))
        if Player==1:
            if MoveColumn<=7:
                if RowMovement_P1.count()==0:
                    print('First Movement!')
                    currentField[MoveColumn][MoveRow]="X"
                    RowMovement_P1[MoveColumn]=MoveRow
                
            


        

    

def DecisionLogic():
    pass

DrawPlayboard(11,15)