import math

def num_BTC(b):
    c = float(0)
    #Document the number of halving events
    n_halves = b // 210000;
    c = 50 * (0.5) ** n_halves * b;
    return c


