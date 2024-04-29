from Bio.SVDSuperimposer import SVDSuperimposer
import numpy as np
import argparse
from scipy.spatial.transform import Rotation as sstR
parser = argparse.ArgumentParser()
parser.add_argument('pdb_list',help='pdb list file needed')
parser.add_argument('BB',help='All Atoms, Backbone atoms, or CA, input keywords: "All", "BB", or "CA"')
parser.add_argument('pw_rmsd',help='output file name')
args = parser.parse_args()
# Type functions because it's helpful.
def get_coords(data):
    atom_types = ["CA", "N", "C", "O"]
    if args.BB == 'CA':
        result = [[float(atm[30:38]),float(atm[38:46]),float(atm[46:54])] for atm in data if atm[13:15]=='CA']
    if args.BB == 'BB':
        result = [[float(atm[30:38]),float(atm[38:46]),float(atm[46:54])] for atm in data if atm[13:15].strip(" ") in atom_types]
    if args.BB == 'All':
        result = [[float(atm[30:38]),float(atm[38:46]),float(atm[46:54])] for atm in data if atm[0:4]=='ATOM']
    return np.array(result)
def read_list(pdb_list):
    return [get_coords(open(f'{pdb}')) for pdb in pdb_list]
def align(native_coords, model_coords):
    """
    Aligns a model structure onto a native structure
    Using the atom types listed in `atom_types`.
    """
    si = SVDSuperimposer()
    si.set(np.array(native_coords), np.array(model_coords))
    si.run() # Run the SVD alignment
    return si.get_rms()
pdb_list = [line.strip('\n') for line in open(f'{args.pdb_list}')]
all_coords = read_list(pdb_list)

f = open(f'{args.pw_rmsd}.txt',"w")
for i,native_coords in enumerate(all_coords[:-1]):
    for model_coords in all_coords[i+1:]:
        f.write('{}'.format(align(np.array(native_coords),np.array(model_coords))))
        f.write('\n')
f.close()
