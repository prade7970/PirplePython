"""
Assignment 3 - If Statement

"""

# function works well with only numbers
def Compare(n1,n2,n3): 
    if n1==n2 or n2==n3:
        return True
    elif n1!=n2 or n2!=n3:
        return False

#Function works with String aswell
def CompareAll(n1,n2,n3):
    if int(n1)== int(n2) or int(n2)==int(n3):
        return True
    elif int(n1)!=int(n2) or int(n2)!=int(n3):
        return False


Result=Compare(6,5,5)
print(Result)
Result2=CompareAll(6,5,"5")
print(Result2)






