import numpy as np

"""
Loads a matrix into a text file.
Input: Matrix and filepath
"""


def writeMatrixToText(matrix, filename):
    np.savetxt(filename, matrix)


"""
Loads a matrix from a text file.
Input: Filepath
Output: matrix
"""


def readMatrixFromText(filename):
    return np.loadtxt(filename)
