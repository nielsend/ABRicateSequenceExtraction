#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 08:28:58 2019


"""
import csv
import os
import sys
#os.chdir('/Users/nielsend/Downloads/GCA_Output')

numArguments = len(sys.argv)
tsv = sys.argv[1] # how to give to pd?
fastaDir = sys.argv[2] 


   

def get_fasta_string(thefilepath, read_start, read_end, accession_input):

    file = str(thefilepath)

    #Convert from strings to int to compare to current char counts.
    read_start = int(read_start)-1 #first char to read
    read_end = int(read_end) #last char to read

    

    fasta_string = ''
    currently_reading = False
    correct_accession = False

    f=open(file, "r")
    for line in f:
        line = line.strip() #remove trailing or leading whitespace for line, e.g. \n or \r (make line naked) 
        if line[0] == ">": #check if first char of line is '>'
            char_count = 0 #restart char count when we get to new accession number 
            header1 = line.split(" ", 1) #get first "word" of header line
            header1 = header1[0][1:] #remove first char (">") of first word to get accession number
            
            if header1 == accession_input:
                correct_accession = True
                continue #don't count first line of file in char count; this is the FASTA header data
            else:
                continue #We dob't want this accession number, so keep going through lines until next header (we didn't set correct_accession to true)
            char_count = 0

        if correct_accession: #correct accession number, so in correct part of file.
            line_length = len(line) 
            placer = char_count + line_length
    
            if currently_reading: #still reading chars to fasta_string
                if read_end > placer: 
					#add entire line to string
					fasta_string = fasta_string + line
                else: #add some of the line up until the read_end point
                    endpoint = char_count + line_length - read_end
                    fasta_string = fasta_string + line[0 : endpoint] #may have to have +1
                    return fasta_string
                    currently_reading = False
			#currently, char_count does not yet include the current line.
            elif placer > read_start >= char_count: #begin reading FASTA string here.
				#if true, we start reading on this line! 
				#start reading at (read_start - char_count)
                fasta_string = "" + line[read_start - char_count : read_end]; 
                currently_reading = True #Now currently reading! Note that if any reading frames are fewer than 80 or so bp, this runs of the risk of having problems...

            char_count += line_length #increment by line length by number of characters on line.



with open(tsv) as tsvfile:
    df = csv.reader(tsvfile, delimiter="\t")

    linecount=0
    for line in df:
        if linecount!=0:
            thefilepath = fastaDir + line[0]
            fileNameOut = line[0]
            accession_input = line[1]
            read_start = line[2]
            read_end = line[3]
            gene = line[4]
            fasta_string = get_fasta_string(thefilepath, read_start, read_end, accession_input)
            print ">" + gene + "~~~" + accession_input + "~~~" + read_start + "~~~" + read_end + "~~~" + fileNameOut 
            print fasta_string
            
#            with open('myfile.txt') as f:
#                header_info = f.readline()
#                open(output_file)
#                output_file.write(header_info, '\n')
#                output_file.write(fasta_string )
#                close(output_file)
                
        linecount=linecount+1





