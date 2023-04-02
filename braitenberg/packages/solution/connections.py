from typing import Tuple

import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    col_values=[0.3, 0.6, 1, -1, -0.6, -0.3]
    numColBlocks = len(col_values)
    for j in range(numColBlocks):
        res[:, j*shape[1]//numColBlocks:(j+1)*shape[1]//numColBlocks]=col_values[j]

    # create row values from 0.1 to 1 with 6 steps
    row_values = np.linspace(0.1, 1, 6)
    numRowBlocks = len(row_values)
    for i in range(numRowBlocks):
        res[i*shape[0]//numRowBlocks:(i+1)*shape[0]//numRowBlocks, :] *= row_values[i]
    
    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")    
    col_values=[-0.3, -0.6, -1, 1, 0.6, 0.3]
    numColBlocks = len(col_values)
    for j in range(numColBlocks):
        res[:, j*shape[1]//numColBlocks:(j+1)*shape[1]//numColBlocks]=col_values[j]

    # create row values from 0.1 to 1 with 6 steps
    row_values = np.linspace(0.1, 1, 6)
    numRowBlocks = len(row_values)
    for i in range(numRowBlocks):
        res[i*shape[0]//numRowBlocks:(i+1)*shape[0]//numRowBlocks, :] *= row_values[i]
    
    return res
      
    return res
