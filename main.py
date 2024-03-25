import random as rd
import numpy as np
import matplotlib.pyplot as plt

def generate_values(n, epoch):
    
    values = []
    
    for i in range(n):
        
        data = []
        
        for i in range(epoch):
        
            r = round(rd.uniform(0,10),1)
            data.append(r)
            
        values.append(data)
    
    return values
            

def rvs(data, n):
    
    max_values = []
    
    for i in range(n):

        local_max = data.index(max(data))
        max_values.append(data.pop(local_max))
        
    return max_values


def get_sorted_data(dataset, n):
    
    sorted_values = []
    
    for d in dataset:
        
        data = rvs(d, n)
        
        sorted_values.append(data)
    
    return sorted_values
    

def get_res(val):
        
    return round(sum(val)/len(val) - 1/2, 3)
    

class Game:
    
    def __init__(self, player_count, data_count, max_values):
        
        self.player_count = player_count
        self.data_count = data_count
        self.max_values = max_values
        
    def _help(self):
        
        res = "These are the functions : "
        res += "get_raw_data() => returns raw data (obviously)"
        res += "get_data() => returns sorted data"
        res += "get_score() => returns the score of each player, in a sorted manner"
        res += "plot_data() => plots all datas"
        
        return "Func broken right now, sry."
        
    def get_raw_data(self):
        
        raw_data = generate_values(self.player_count, self.data_count)
        return raw_data
    
    def get_data(self):
        
        raw_data = generate_values(self.player_count, self.data_count)
        sorted_data = get_sorted_data(raw_data, self.max_values)
        return sorted_data
    
    def get_score(self):
        
        raw_data = generate_values(self.player_count, self.data_count)
        sorted_data = get_sorted_data(raw_data, self.max_values)
        score = rvs([get_res(data) for data in sorted_data], len(sorted_data))
        return score
    
    def plot_data(self):
        
        raw_data = generate_values(self.player_count, self.data_count)
        sorted_data = get_sorted_data(raw_data, self.max_values)
        
        for data in sorted_data:
        
            plt.plot(np.linspace(1,len(data),len(data)),np.array(data))
        
        plt.show()

