import numpy as np
import pandas as pd

def get_values(filename):
    type_ = input('[m]ean or [s]um? > ').strip().lower()
    if type_ == 'm':
        return _get_means(filename)
    else:
        return _get_sums(filename)

def _get_means(filename):
    '''
    INPUT: filepath
    OUTPUT: Numpy ndarray with MEAN values for the train dataset and the original target matrix as Numpy ndarray
    '''
    df = pd.read_csv(filename)
    return np.array([[df.mean()[1], df.mean()[2], df.mean()[2], df.mean()[4], df.mean()[5]]]), df.as_matrix()

def _get_sums(filename):
    '''
    INPUT: filepath
    OUTPUT: Numpy ndarray with SUM values for the train dataset by rows and the original target matrix as Numpy ndarray
    '''
    df = pd.read_csv(filename)
    df['sums'] = df.sum(axis=0)
    return df.sums.as_matrix(), df.as_matrix()

if __name__ == "__main__":
    filename = '..data/Train/train.csv'
    target_val_array, target_matrix = get_values(filename)
