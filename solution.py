import pandas as pd
import numpy as np


chat_id = 736941004 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    n = len(x)
    t = 10
    X = np.ones((n, 2))
    X[:, 0] = t
    Y = x
    a, c = np.linalg.lstsq(X, Y, rcond=None)[0]
    return a
