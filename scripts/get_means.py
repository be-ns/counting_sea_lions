import numpy as np
import pandas as pd

def df_and_describe(filename):
    '''
    INPUT: filepath
    OUTPUT: mean number of adult_males, subadult_males, adult_females, pups for each image in our train set.
    '''
    df = pd.read_csv(filename)
    return df.mean()[1], df.mean()[2], df.mean()[2], df.mean()[4], df.mean()[5]

if __name__ == "__main__":
    filename = '/Users/benjamin/Desktop/TrainSmall2/Train/train.csv'
    adult_males, subadult_males, adult_females, pups = df_and_describe(filename)
