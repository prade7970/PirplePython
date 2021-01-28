import os

class DrawHangManGallows:
    def __init__(self):
        pass
    
    def hangmanstages(self):
        intial_gallow = "----------\n |\t|\n\t|\n\t|\n\t|\n\t|\n\t|\n\t-------------"
        hangman= [ "----------\n |\t|\n 0\t|\n\t|\n\t|\n\t|\n\t|\n\t-------------",
          "----------\n |\t|\n 0\t|\n |\t|\n\t|\n\t|\n\t|\n\t-------------",
          "----------\n |\t|\n 0\t|\n-|\t|\n\t|\n\t|\n\t|\n\t-------------",
          "----------\n |\t|\n 0\t|\n-|-\t|\n\t|\n\t|\n\t|\n\t-------------",
          "----------\n |\t|\n 0\t|\n-|-\t|\n/\t|\n\t|\n\t|\n\t-------------",
          "----------\n |\t|\n 0\t|\n-|-\t|\n/ \ \t|\n\t|\n\t|\n\t-------------"
         ]
        print(intial_gallow) 
        return hangman
                     
    

class ChooseMode:
    def __init__(self):
        pass
    def ChooseModeFunc(self):
        user_input= int(input("One Player(1) or Two Player mode(2)"))
        if user_input==2:
            Word=input("Two Player Mode Selected: - Player 1 pick a word : ")
            #print("Answer",Word)
            #BlankSpaces= len(Word)
        return user_input,Word
            

class TwoPlayerMode:
    def __init__(self):
        pass
    
    def GameBegins(self,secret_word):
    
        display_hangman=0
        secret_list=[]
        display_correct_guess=[]
        index_pos_list=[]
        correct_guess=[]
        cg=[]
        secret_list= list(secret_word.lower())
        hangmanstages=[ "----------\n |\t|\n 0\t|\n\t|\n\t|\n\t|\n\t|\n\t-------------",
          "----------\n |\t|\n 0\t|\n |\t|\n\t|\n\t|\n\t|\n\t-------------",
          "----------\n |\t|\n 0\t|\n-|\t|\n\t|\n\t|\n\t|\n\t-------------",
          "----------\n |\t|\n 0\t|\n-|-\t|\n\t|\n\t|\n\t|\n\t-------------",
          "----------\n |\t|\n 0\t|\n-|-\t|\n/\t|\n\t|\n\t|\n\t-------------",
          "----------\n |\t|\n 0\t|\n-|-\t|\n/ \ \t|\n\t|\n\t|\n\t-------------"
        ]
    
        for i in range(len(secret_list)):
            if secret_list[i]==' ':
                #print('-',end="")
                display_correct_guess.append('- ')
            else:
                display_correct_guess.append('_ ,')
        print(display_correct_guess)
   
        while(True):
        #for i in range(len(hangmanstages)):
            guess=input('Guess : ')
            if guess.lower() in secret_list:
                correct_guess.append(guess.lower())
                for j in range(len(secret_list)):
                    if secret_list[j]==guess.lower():
                        index_pos_list.append(j)
                    #cg.insert(guess.lower(),str(index_pos_list))
                        if j==len(secret_list):
                            print("You Guessed all correctly",secret_word)
                            break
                        break
                print("You guessed right!", "Word is at", str(index_pos_list))
                
            else:
                if(display_hangman<len(hangmanstages)):
                    print(hangmanstages[display_hangman])
                    display_hangman+=1
                if(display_hangman==len(hangmanstages)):
                    print("You Lost!")
                    break
        
class SinglePlayerMode:
    def __init__(self):
        pass

if __name__ == "__main__":
    cm=ChooseMode()
    userinput,secret_word=cm.ChooseModeFunc()
    tw= TwoPlayerMode()
    print(chr(27) + "[2J")
    d=DrawHangManGallows()
    hangmanstages=d.hangmanstages()
    #tw.DrawBlankSpaces(secret_word)
    tw.GameBegins(secret_word)



