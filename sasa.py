import argparse
from Bio.PDB import PDBParser
from Bio.PDB.SASA import ShrakeRupley
parser = argparse.ArgumentParser()
parser.add_argument('file',help='pdb file needed')
args = parser.parse_args()
struct = PDBParser(QUIET=True).get_structure('ab','{}'.format(args.file))
sr = ShrakeRupley()
sasa = []
for alt_model in struct:
    sr.compute(alt_model,level="C")
    sasa.append(alt_model["a"].sasa)
with open('{}.sasa'.format((args.file).partition('.')[0]),'w') as f:
    for ele in sasa:
        f.write('%s\n'%ele)
