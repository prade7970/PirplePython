
"""a= ["----------\n |\t|\n\t|\n\t|\n\t|\n\t|\n\t|\n\t-------------"]
print(a[0])
b=["----------\n |\t|\n 0\t|\n\t|\n\t|\n\t|\n\t|\n\t-------------"]
print(b[0])
c=["----------\n |\t|\n 0\t|\n |\t|\n\t|\n\t|\n\t|\n\t-------------"]
print(c[0])

d= ["----------\n |\t|\n 0\t|\n-|\t|\n\t|\n\t|\n\t|\n\t-------------"]
print(d[0])

e=["----------\n |\t|\n 0\t|\n-|-\t|\n\t|\n\t|\n\t|\n\t-------------"]
print(e[0])

f=["----------\n |\t|\n 0\t|\n-|-\t|\n/\t|\n\t|\n\t|\n\t-------------"]
print(f[0])                 

g=["----------\n |\t|\n 0\t|\n-|-\t|\n/ \ \t|\n\t|\n\t|\n\t-------------"]
print(g[0])
"""
"""
hangman= ["----------\n |\t|\n\t|\n\t|\n\t|\n\t|\n\t|\n\t-------------",
          "----------\n |\t|\n 0\t|\n\t|\n\t|\n\t|\n\t|\n\t-------------",
          "----------\n |\t|\n 0\t|\n |\t|\n\t|\n\t|\n\t|\n\t-------------",
          "----------\n |\t|\n 0\t|\n-|\t|\n\t|\n\t|\n\t|\n\t-------------",
          "----------\n |\t|\n 0\t|\n-|-\t|\n\t|\n\t|\n\t|\n\t-------------",
          "----------\n |\t|\n 0\t|\n-|-\t|\n/\t|\n\t|\n\t|\n\t-------------",
          "----------\n |\t|\n 0\t|\n-|-\t|\n/ \ \t|\n\t|\n\t|\n\t-------------"
         ]

for i in range(7):
    print(hangman[i])


for i in range(len(Word)-1):
                if Word[i]== " ":
                    print("- ",end="")
                
                print('__ ,',end="")
"""

def GameBegins(secret_word,hangman):
        i=0
        while(True):
            i=0
            guess=input('Letter: ')
            sw=secret_word.lower()
            print(sw)
            for i in range(len(secret_word.lower())+1):
                if guess in sw:
                    print(guess, sw.index(guess))
                    break
                else:
                    print(hangman[i])
                    i+=1
                    break

secret_word= input('Enter ')

hangman= [ "----------\n |\t|\n 0\t|\n\t|\n\t|\n\t|\n\t|\n\t-------------",
          "----------\n |\t|\n 0\t|\n |\t|\n\t|\n\t|\n\t|\n\t-------------",
          "----------\n |\t|\n 0\t|\n-|\t|\n\t|\n\t|\n\t|\n\t-------------",
          "----------\n |\t|\n 0\t|\n-|-\t|\n\t|\n\t|\n\t|\n\t-------------",
          "----------\n |\t|\n 0\t|\n-|-\t|\n/\t|\n\t|\n\t|\n\t-------------",
          "----------\n |\t|\n 0\t|\n-|-\t|\n/ \ \t|\n\t|\n\t|\n\t-------------"
         ]
GameBegins(secret_word,hangman)