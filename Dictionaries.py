
""""
Return to your first homework assignments, when you described your favorite song. 
Refactor that code so all the variables are held as dictionary keys and value. 
Then refactor your print statements so that it's a single loop that passes through
each item in the dictionary and prints out it's key and then it's value.

Create a function that allows someone to guess the value of any key in the dictionary,
 and find out if they were right or wrong. This function should accept two parameters: 
 Key and Value. If the key exists in the dictionpary and that value is the correct value,
  then the function should return true. In all other cases, it should return false.

"""

SongDictionary ={'songName' :"Feliz Navidad", 'SongDuration': '10' ,'songGenre':"Christmas", 'songWriter': "Anonymous" }

print(SongDictionary)

def GuesstheSong(key,value):
    while True:
        #print(value)
        #x=input('Enter Attribute(Key) you want to search, -1 to exit')
        #y=input('Enter Value for the Attribute' + str(x) , + '-1 to exit')
        if key==-1 or value==-1:
            break
        if key in SongDictionary and value in SongDictionary[key]:
            #print('Correct Combination Guess')
            return True
        else:
            #print('Incorrect')
            return False            
        
        
        
        

key=input('Enter Attribute(Key) you want to search, -1 to exit')
value=input('Enter Value for the Attribute' + str(key)  + '-1 to exit')

GuesstheSong(key,value)



