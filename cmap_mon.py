"""
Simple script showing an example intra-peptide contacts calculation.
Contact: s.samantray@fz-juelich.de
"""

import numpy as np
import copy as cp
import subprocess as sp
import os as os
import shutil as sh
import MDAnalysis as mdana
import sys
from MDAnalysis.analysis.distances import distance_array

# Some variables
#ff = sys.argv[1]
r=sys.argv[1]
#Atoms = int(sys.argv[2])
#system = sys.argv[3]
Atoms = 134
AminoAcids = 7
AtomsperAminoAcid = [1, 29, 48, 64, 84, 104, 114, 135]
MinD = 4 # Distance in Angstrom than defines if two amino acids are in contact
MolDir = '/u2/data/suman/Analysis-paper/monomer/a99-disp/wt/r'+ r

AtomGroups = []

# Create contact matrix
ContactMap = [[0 for x in range(AminoAcids)] for y in range(AminoAcids)]

# Calculate contact matrix
os.chdir(MolDir)

# Create Universe
uni = mdana.Universe('prod-a99disp.pdb','prod-a99disp.xtc')

# Create atom groups for each amino acid of each monomer
for aa in range(0,AminoAcids):
	AtomGroups.extend([uni.select_atoms('bynum '+str( AtomsperAminoAcid[aa])+':'+str( AtomsperAminoAcid[aa + 1] - 1 ))])

count = 0
# Analyse trajectory
for n,t in enumerate(uni.trajectory):
	if n > 0:
        	# Calculate dimension of the box to considerd PBC
		box = t.dimensions[:6]
		count += 1
		for n2,atoms1 in enumerate(AtomGroups):
			for n3,atoms2 in enumerate(AtomGroups):
				if ((distance_array(atoms1.positions,atoms2.positions,box).min()) <= MinD):
					ContactMap[n2][n3] +=1
					ContactMap[n3][n2] +=1 

#print (count)
# Save contact map in a file
fileout = open ('cmapfinal-mon.dat','w')
for i in ContactMap:
	for j in i:
		fileout.write (str(float(j)/float(count)/2.0) + '\t')
	fileout.write ('\n')
fileout.close()

