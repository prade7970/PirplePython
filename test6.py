
def GameBegins(secret_word):
    
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
       


        
        

    
    
        

         
            
       
        
GameBegins('Hello World')