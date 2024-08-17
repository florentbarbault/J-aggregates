# J-aggregates

This repository help you to identify and count J-aggregates of a molecular dynamics trajectory.

This software uses the cpptraj program from the AMBER suite. This software is free and available on the website: https://ambermd.org/

J-aggregates are defined using geometric criteria taken from *Chem. Rev. 2018, 118, 7069-7163*, taking into account the angle of inclination of the aromatic rings. Please note that this is a research program, which means that it certainly needs to be adapted to your needs. 

The repo contains several programs for download

1. **Script_gener-cpptraj.py**
2. **J-AGGREGATES.sh**
3. **Count_J-aggregates.py**

You first have to modify **Script_gener-cpptraj.py** to your needs. Basically, it creates the long list of distances and angles that will be determined by cpptraj. Then, the soft **J-AGGREGATES.sh** simply execute cpptraj and **Count_J-aggregates.py**.

If this soft is useful for you, please cite: XXXXXXXXXXXXXXXXX
