# Incremental Community Detection: A game-theoretic approach

This is an open-source repository for the work of a Bachelor's Thesis in Incremental Community Detection: A game-theoretic approach
The goal is to apply community detection on undirected, unweighted incremental networks utilising Game Theory.

### Environment:
This code is compiled with Python 3.9 in a virtual environment. The code was executed on an M1 MacBook Pro with 8 cores and 8 GB of RAM, running macOS Sonoma 14.2.1.

### Packages
Packages required to run this code:
- numpy
- [numba](https://numba.pydata.org)


### Instructions
Examples are found in the "Tests" directory and in the main.py. 
- Initiate an adjacency matrix with one of the available function 
- call  a runCD function from algorithm.py, with the adjacency matrix and a similarity list file path (optional)
- writeAndReadSimilarityToFile.py includes 2 functions to read and write a calculated similarity list to/from a file

### References

The algorithmic groundwork was taken from Alvari et al.[1] and build upon. 
Tracked metrics as the Discrete Fourier Transformation as proposed by Zhu et al.[2] were utilised to improve the algorithm's convergence.
Additionally, the datasets for the tests were provided by DynGraphLab[3].

### Bibliography

[1] Alvari, Hamidreza, Alireza Hajibagheri, and Gita Sukthankar. "Community detection in dynamic social networks: A game-theoretic approach." 2014 IEEE/ACM International Conference on Advances in Social Networks Analysis and Mining (ASONAM 2014). IEEE, 2014.

[2] Zhu, Yunyue, and Dennis Shasha. "Statstream: Statistical monitoring of thousands of data streams in real time." VLDB'02: Proceedings of the 28th International Conference on Very Large Databases. Morgan Kaufmann, 2002.

[3] Hanauer, Kathrin, Monika Henzinger, and Christian Schulz. "Recent advances in fully dynamic graph algorithms." arXiv preprint arXiv:2102.11169 (2021).