import math

def num_BTC(b):
    c = float(0)
    #Document the number of halving events
    n_halves = b // 210000
    #Document the initial reward per block
    rewardPerBlock = 50
    while(n_halves > 0):
        c = c + rewardPerBlock * 210000
        n_halves--
        rewardPerBlock = rewardPerBlock * 0.5
    
    c = c + (b % 210000) * rewardPerBlock
    
    return c


