mport sys
import os
import functools
if(len(sys.argv) != 2):
print ("Invalid Arguments")
sys.exit()
if(not(os.path.exists(sys.argv[0]))):
print ("Invalid File Path")
sys.exit()
if(sys.argv[1].split('.')[-1] != "txt"):
print ("Invalid File Format. Only TXT files allowed")
sys.exit()
escape = open(sys.argv[1])
worddic = { }
 
for line in escape: #Outer for loop - taking each line in the file
 
myline = line.split()  
 
for word in myline: #Inner for-loop processing each line
w = worddic.get(word,0)  
 
 
worddic[word] = w + 1 #Incrementing the word count, if the word exists
 
print ("\n Result of storing number of occurances of word in dictionary \n", worddic ,"\n ")
 
sortedlist = [ ]
sortedlist = sorted(worddic.items(), key = lambda Y : Y[1], reverse = True)
print ("\n Sorting in Dscending order of Value Occurance - \n" )
for n in range(0,10):
print (sortedlist[n], "\n")
 
lenlist = []
print ("\n Length of each word in a list \n")
for i in range(len(sortedlist)):
wordTuple = sortedlist[i]
print ("\n ", wordTuple[0], ", Frequency: " , wordTuple[1] , ", Length " ,
len(wordTuple[0]))
lenlist.append(len(wordTuple[0]))
 
mysum = functools.reduce(lambda x, y: x + y, lenlist)
print ("\n Average length of all words: " , mysum/len(lenlist))
 
squares = [x**2 for x in lenlist if x%2 != 0]
print ("\n Squres of odd word lengths: ")
print (squares)