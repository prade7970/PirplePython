numbers=[] #Empty List
myUniqueList=[] #Empty Unique List
myleftovers=[] #Empty non unique list

def AddToList(n1): #Function to add to numbers list
    numbers.append(n1)
    AddOnlyUniqueueElements(numbers) #Call to Function for Unique

def AddOnlyUniqueueElements(n1): #Filter out Unique
     #myUniqueList=[] 
    for number in numbers:
        if number in myUniqueList:
            myleftovers.append(number)
            continue
        else:
            myUniqueList.append(number)
        
    return myUniqueList              

AddToList(10)
AddToList(20)
AddToList(10)

    
    
        
   






#AddToUniqueList(10)
#AddToUniqueList(10)

print(myUniqueList)
print(myleftovers)
    


    

    
    

