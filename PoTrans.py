#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Course: Python programming for life science researchers VT19
#Project: Potential Transcripts Prediction
#Author: Yarong Tian

#Import the original data
#sequence=input("Please paste query sequence here:")
sequence="TATACGTATAGGCTAATAAACCCAATAAA"


#Read the query sequence
seq=str(sequence)


ResultHead = ['StartPosition', 'NumberOfTranscripts']
print(ResultHead)

#Function on the pol II promoter
#def find_TATA(countseq, start):  
    #SP = countseq.find(start,beg=i,end=len(countseq))
    #return SP  

#Count number of possible polyA signal        
#def count_transcripts(rest_seq, end):
    #NOTs = rest_seq.count(end)
    #return NOTs    

#Count of Potential Transcripts       
for i in range(len(seq)):
    #print(i)
    start = "TATA"
    end = "AATAAA"
    countseq=seq[i:]
    #if i == 0
    SP = seq.find(start,i,len(seq))
    if SP == -1:
        break
    rest_seq = seq[SP+4:]
    NOTs = rest_seq.count(end)
    Result = [SP, NOTs]
    print(Result)
    
    STARTrest = rest_seq.count(start)
    #print(STARTrest)
    if STARTrest == 0:
        break
    
    
   # if SP != -1:
    #    i = i + len(start)
     #   rest_seq = seq[i:] 
     #   NOTs = rest_seq.count(end)
     #   SP = countseq.find(start,i,len(countseq))
     #   print(rest_seq)
     #   print(NOTs)
    #else: 
    #    break
  
    
    #rest_seq = seq[SP+len(start):]
    #NOTs = rest_seq.count(end)
    #print(countseq)
    #print(SP)
    #print(NOTs)
    
    
    #Result = [str(i+1), str(SP), str(NOTs)]
    #countseq = seq[fin]

#print(Result)
#Ord += 1
        
















