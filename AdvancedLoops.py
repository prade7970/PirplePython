"""
Advanced Loops
Draw playboard

"""

#import os
#print(os.get_terminal_size()) #columns - 123 % lines -23


#  | |     1
# ------   2
#  | |     3
# ------   4 
#  | |     5

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
                print('-----------')
          
    else:
        return False


     


DrawPlayboard(4,5)
DrawPlayboard(24,124)

