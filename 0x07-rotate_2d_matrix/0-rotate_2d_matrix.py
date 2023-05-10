#!/usr/bin/python3
'''3D matrix
'''


def rotate_2d_matrix(matrix):
    """The function"""
    rep_matrix = []
    for i in range(len(matrix)):
        sub_matrix = []
        for j in range(len(matrix)):
            itr = len(matrix) - (j + 1)
            sub_matrix.append(matrix[itr][i])
        rep_matrix.append(sub_matrix)
    for i in range(len(matrix)):
        matrix[i] = rep_matrix[i]
