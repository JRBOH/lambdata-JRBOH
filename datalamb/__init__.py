import numpy as np
import pandas as pd

def null_kill(X):
    '''a helper that kills null values and their friends'''
    X = X.copy()

    X = X.dropna()

    return X