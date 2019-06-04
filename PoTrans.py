#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Course: Python programming for life science researchers VT19
# Project: Potential Transcripts Prediction
# Author: Yarong Tian

# Import the original data
sequence=input("Please paste query sequence here: ")

# Read the query sequence
seq=str(sequence)

# Prepare for printing the head of the results
ResultHead = ['RESULTS: ','StartPosition', 'NumberOfTranscripts']

# Define the start and end sequences
start = "TATA"
end = "AATAAA"

# Build a dictionary
result = {}

# Count Potential Transcripts       
for i in range(len(seq)):
    
# Find() method is used to find the starting index of the start string(TATA) in the 
# substring beginning at index(i) and ending at the end of sequence(seq)
    SP = seq.find(start,i,len(seq))
    
    # Stop when there is no start string(TATA).
    if SP == -1:
        break
    
    # Name the subsequence after the start string(TATA) as rest_seq
    rest_seq = seq[SP+len(start):]
    
    # The inbuilt string count() funtion is used to count how many times the end 
    # string(AATAAA) exist in the rest_seq
    NOTs = rest_seq.count(end)
    
    # Pair the values in the dictionary result
    result[SP] = NOTs
    
    # When there is no the end string(AATAAA) in the rest_seq, then stop
    if NOTs == 0:
        break
    
# Print the result to screen
# Print the result heads
print(ResultHead[0],'\n',ResultHead[1],'\t',ResultHead[2])

# Print the result values
for key in result:
    print(key, '\t', '\t', result[key])
    

    




    
        
















