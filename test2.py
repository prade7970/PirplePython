import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    s_l= list(s)
    count_l=[]
    #d={}
    count=0
    j=0
    for i in range(len(s_l)):
       c=s_l.count(s[i])
       count_l.append(c)
       if j<3:
           count_l.sort(reverse=True)
           j+=1
    print(count_l)
       
      
             
    
      
     
       
       
       