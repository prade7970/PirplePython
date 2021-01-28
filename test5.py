
def GameBegins(secret_word):
    #while(True):
       # g=input('Guess')
    hangman= [ "----------\n |\t|\n 0\t|\n\t|\n\t|\n\t|\n\t|\n\t-------------",
          "----------\n |\t|\n 0\t|\n |\t|\n\t|\n\t|\n\t|\n\t-------------",
          "----------\n |\t|\n 0\t|\n-|\t|\n\t|\n\t|\n\t|\n\t-------------",
          "----------\n |\t|\n 0\t|\n-|-\t|\n\t|\n\t|\n\t|\n\t-------------",
          "----------\n |\t|\n 0\t|\n-|-\t|\n/\t|\n\t|\n\t|\n\t-------------",
          "----------\n |\t|\n 0\t|\n-|-\t|\n/ \ \t|\n\t|\n\t|\n\t-------------"
         ]  
    list_sw=list(secret_word.lower())
    correct=[]
    position=[]
    blank=[]
    j=0
    index_pos=0
    tries=0
    while(tries<=len(hangman)+1):
        guess=input('Enter')
        i=0
        for i in range(len(list_sw)):
            #print(list_sw[i])
            #print(guess.lower())
            while(True):
                try:
                    if (guess.lower() in list_sw):
                        #print("Correct",list_sw)
                        correct.append(guess.lower())
                        index_pos=list_sw.index(guess.lower(),index_pos)
                        position.append(index_pos)
                        index_pos+=1
                        #position.append(list_sw.index(guess.lower()))
                        #position+=1
                        print(correct)
                        print(position)
                        blank.append('_')
                        tries+=1
                        break
                    else:
                        print("Incorrect",list_sw)
                        break
                except ValueError as e:
                    break
               

"""       
j=0
while(j<=5):
print("Incorrect",guess.lower())
print(hangman[j])
j+=1
break   
"""             
            



GameBegins('Hi Vi')