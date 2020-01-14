#!/usr/bin/env python3
import argparse
import os
import random
#importing libraries

#parser = argparse.ArgumentParser(description = "please give a header")
#parser.add_argument("-h", "-header")
#args = parser.parse_args()

nuc_list= ["A","T","C","G"]

def repeat_seq(length):
#function that makes random seq od nucleotides in a specific range
    your_letters='ATCG'
    return ''.join((random.choice(your_letters) for i in range(length)))

repeat_seq1=repeat_seq(30)
repeat_seq2=repeat_seq(30)
repeat_seq3=repeat_seq(30)
repeat_seq4=repeat_seq(30)
repeat_seq5=repeat_seq(30)

def new_fasta(): 
#try block is skipping error and makes the code continue on with what it can
	try:
		with open("psuedo_protein.fasta","w") as in_handle:
			#in_handle.write(args.header)
#			print(in_handle)
#			in_handle.write("\r")
#			print(in_handle)
			in_handle.write(repeat_seq1)
			in_handle.write(repeat_seq1)
			in_handle.write(repeat_seq2)
			in_handle.write(repeat_seq3)
			in_handle.write(repeat_seq4)
			in_handle.write(repeat_seq5)
			in_handle.write(repeat_seq2)
			in_handle.write(repeat_seq3)
			in_handle.write(repeat_seq4)
			in_handle.write(repeat_seq5)
		return(in_handle)

	except IOError as err:
#this is the exception error that will help the code
		print("IOError")
#calling function
print(new_fasta())
