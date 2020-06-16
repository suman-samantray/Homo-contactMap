"""
Simple script showing an example intra-peptide contacts calculation.
Contact: s.samantray@fz-juelich.de
"""

import numpy as np
import sys
import os


base_filename, suffix = os.path.splitext(sys.argv[1])
f_in=open(sys.argv[1], "r")       #opens a file in the reading mode

in_lines=f_in.readlines()      #reads it line by line
out=[]
for line in in_lines:
    list_values=line.split()   #separate elements by the spaces, returning a list with the numbers as strings
    for i in range(len(list_values)):
        list_values[i]=eval(list_values[i])     #converts them to floats
#       print list_values[i],
        if list_values[i]==1:     #your condition
#           print ">>", 1
            list_values[i]=0
    out.append(list_values)         #stores the numbers in a list, where each list corresponds to a lines' content
f_in.close()                        #closes the file


new_filename= os.path.join(base_filename+ "_n" + suffix)
f_out=open(new_filename, "w")     #opens a new file in the writing mode
for cur_list in out:
    for i in cur_list:
        f_out.write(str(i)+"\t")    #writes each number, plus a tab
    f_out.write("\n")               #writes a newline
f_out.close()                       #closes the file
