#!/usr/bin/env python3
import argparse
import FileIO
import Random
import OS
import random
#importing libraries

#parser = argparse.ArgumentParser
nuc_list= ["A","T","C","G"]

def repeat_seq(length):
    your_letters='ATCG'
    return ''.join((random.choice(your_letters) for i in range(length)))

repeat_seq1=repeat_seq(30)
repeat_seq2=repeat_seq(30)
repeat_seq3=repeat_seq(30)
repeat_seq4=repeat_seq(30)
repeat_seq5=repeat_seq(30)

def new_fasta(): 
	try:
		with open("psuedo_protein.fasta",w) as in_handle:
			in_handle.write(repeat_seq1, repeat_seq2, repeat_seq3, repeat_seq4, repeat_seq5)


	except as IOError:
	#this is the exception error that will help the code
		print("IOError")
