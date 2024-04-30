# DMD Simulation Analysis Utilities

## **Introduction**
Welcome to the GitHub repository dedicated to providing essential data analysis utilities for discrete molecular dynamics (DMD) simulations. DMD simulations are recognized for their superior sampling efficiency and have become a cornerstone in computational biomolecular research.

For those interested in conducting DMD simulations, access to a dedicated simulation platform is available at [DMD](http://www.moleculesinaction.com).

The utility scripts included in this repository are designed to handle large datasets generated from DMD simulations, particularly focusing on protein-protein interactions. These scripts offer functionalities such as:

- Conformational clustering
- Analysis of dihedral angle distributions
- Calculation of the ensemble average of residue-wise secondary structure propensity
- Identification of β-sheet layers distribution
- Determination of the solvent-accessible surface area of a protein PDB file across extensive frames

These utilities aim to streamline the analysis process and provide researchers with valuable insights into the dynamics and interactions within biomolecular systems simulated via DMD.

## **Dependencies**
Python 3.6 or later versions are recommended. The version of dependencies may vary depending on the Python version.
- [Numpy](https://pypi.org/project/numpy/)
- [Pandas](https://pypi.org/project/pandas/)
- [Argparse](https://pypi.org/project/argparse/)
- [Biopython](https://pypi.org/project/biopython/)
- [tqdm](https://pypi.org/project/tqdm/)
- [SciPy](https://pypi.org/project/scipy/)
- [Matplotlib](https://pypi.org/project/matplotlib/)

Make sure you have these dependencies installed before running the scripts.
## **Usage**
Clone this repository to your local machine:
```bash
git clone https://github.com/songzhihenry/DMD-simulation-analysis-method
```
### **Clustering**
The file *HC_on_ctm_with_label.ipynb* performs hierarchical clustering upon residue contacts, aiming to provide insight into protein-protein interaction.  
*PW_RMSD.py* computes pair-wise RMSD of structures, of which paths should be listed in a file line by line.
```bash
python PW_RMSD.py pdb_list all output
```
Herein, "all" refers to using all-atom positions for RMSD calculation. Alternatively, "BB" and "CA", denoting the calculation upon positions of backbone atoms and alpha-carbon, can be used to reduce the computational cost but lower accuracy.
### **Dihedral angles**
### **Residue-wise SS**
### **β-sheet layer distribution**
