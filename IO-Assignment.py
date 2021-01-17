"""
Note Taking program
"""
import os
from os import path

def NoteTaking():
    print('Starting up!')
    filename=input('Enter the name of file you want to create')
    #Check if file exists
    if(path.exists(filename)):
        print("File exists")
        option= int(input('1.Read File, 2.Delete File&StartOver ,3: Append, 4: Replace'))
        if option==1:
            File=open(filename,"r")
            print(File.read())
            File.close()
        if option==2:
            print("Deleting" + filename)
            os.remove(filename)
        if option==3:
            File=open(filename,"a")
            text=input("Enter the text you want to add in the file!")
            File.write('\n'+ text)
            File.close()
        if option==4:
            return pass


        
    else:
        print('File Doesnt Exist')
        text=input("Enter the text you want to add in the file!")
        File=open(filename,"r+")
        File.write(text)
        File.close()
        


NoteTaking()

    