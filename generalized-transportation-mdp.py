# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 14:01:35 2022

@author: aaaro
"""

class TransportationMDP(object):
    
    def __init__(self, N):
        
        #N = number of blocks
        
        self.N = N
        
    def startState(self):
        
        # where we are starting
        
        return(1)
    
    def isEnd(self, state):
        
        # did we reach where we needed to be?
        
        return(self.N == state)
    
    def actions(self, state):
        
        # returns a list of valid actions
        
        results = []
        
        if state + 1 <= self.N:
            
            results.append('walk')
            
        if state * 2 <= self.N:
            
            results.append('tram')
            
        return(results)
    
    def succProbReward(self, state, action):
        
        # returns tuple of (s', prob, reward)
        
        # s = state
        # a = action
        # s' = new state
        
        # prob = T(s, a, s')
        
        # reward = Reward(s, a, s')
        
        result = []
        
        if action == 'walk':
            
            result.append((state + 1, 1, -1))   #reward = -1: walking 1 block takes 1 unit of time
            
        elif action == 'tram':
            
            result.append((state*2, 0.5, -2)) #reward = -2: 1 tram ride takes 2 units of time, but you travel state*2 blocks, assuming the tram doesn't fail. p(fail) = 0.5
            result.append((state, 0.5 -2)) #if the tram failes, we remain where we are and lose the time.
            
        return(result)
    
    def discount(self):
        
        return(1)
    
    
    def states(self):
        
        return(range(1, self.N + 1))
    
    
mdp = TransportationMDP(N = 10)
mdp.actions(3)
mdp.succProbReward(state = 3, action = 'walk')
mdp.succProbReward(state = 3, action = 'tram')