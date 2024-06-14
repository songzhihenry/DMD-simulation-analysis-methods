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
Make sure you have *Awk* installed and can be used directly via command line.
## **Usage**
Clone this repository to your local machine:
```bash
git clone https://github.com/songzhihenry/DMD-simulation-analysis-method
```
### **Clustering**
*Ref_RMSD.py* computes RMSD of structures to a reference structure (e.g., native structure).
```bash
python Ref_RMSD.py ref_pdb pdb_list all output
```
Herein, "ref_pdb" refers to the structure as the referecne. "pdb_list" should be a path to a file that includes pdb structures that you would like to compute RMSD for. "all" refers to using all-atom positions for RMSD calculation. Alternatively, "BB" and "CA", denoting the calculation upon positions of backbone atoms and alpha carbon, can be used to reduce the computational costs but lower accuracy.  

The file *HC_on_ctm_with_label.ipynb* performs hierarchical clustering upon residue contacts, aiming to provide insight into protein-protein interaction.  
*PW_RMSD.py* computes pair-wise RMSD of structures, of which paths should be listed in a file line by line. The pair-wise RMSD result will be used for further clustering.  
```bash
python PW_RMSD.py pdb_list all output
```
Herein, "ref_pdb" refers to the structure as the referecne. "pdb_list" should be a path to a file that includes pdb structures that you would like to compute RMSD for. "all" refers to using all-atom positions for RMSD calculation. Alternatively, "BB" and "CA", denoting the calculation upon positions of backbone atoms and alpha carbon, can be used to reduce the computational costs but lower accuracy.
```bash
(echo "1000" && cat output) > ocinput
```
"1000" should be changed to the number of structures you would like to cluster. 
```bash
python hierarchy_clustering.py ocinput n_clusters method
```
You may be able to customize *n_clusters* based on your demand. *method* includes single(min), complete(max), average(mean), centroid, median, ward. Please choose the one that you think is better for your case.  
The results of HC will be cluster numbers alongside size and centroid id in your terminal. Meanwhile, you should be able to see a dendrogram produced in your current working directory.
### **Dihedral angle in Ramachandran plot**
*dihedral_angles.ipynb* collects dihedral angles of example structures in directories crystal_stru and fibril_stru, and plot them in a Ramachandran plot. The notebook further computes structures of which PDB files contain massive frames and draws both scattered points and distribution densities.
### **Residue-wise secondary structures**
*RW_2ndcal_trj_mean.awk* script can rapidly calculate mean values and standard deviations of 4 types of secondary structure for each residue of proteins of interest extracted from DMD simulations. The script can run directly in the way of a one-liner command line.
```bash
gawk -f RW_2ndcal_trj_mean.awk -F"!" 30000 50 filename.dssp > SS_output.txt
```
"-F" is for the peptide separation; "30000" refers to the total frames of the simulation output. "50" denotes the number of simulation trajectories.
### **β-sheet layer distribution**
*beta_layer.ipynb* is the notebook for the computation of β-sheet layer distribution, which requires raw data of cluster and DSSP complex analysis outputs. The function defined in the notebook can recognize the chain IDs of clusters formed during the simulation. Furthermore, the function can adjust cluster size according to the DSSP file, ensuring all chains adopt β-sheet conformations. Moreover, the function counts the number of β-sheets that are not connected to each other for each  β-sheet cluster and each frame. At the end of the day, it collects β-sheet layer information frame-by-frame for further stastical computation.
