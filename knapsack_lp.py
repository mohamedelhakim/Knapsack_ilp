# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 17:27:04 2021

@author: mohamed elhakim
"""
from pulp import *
import numpy as np

class KNAPSACKILP:
    def __init__(self,value,weight,capacity,number_of_items):
        self.value=value
        self.weight=weight
        self.capacity = capacity
        self.number_of_items=number_of_items
        self.model = LpProblem("KNAPSACK", LpMaximize)
        self.variable_names = [str(i) for i in range(0, number_of_items)]
        self.DV_variables = LpVariable.matrix("X", self.variable_names, cat = "Integer", lowBound= 0 )
        self.allocation = np.array(self.DV_variables)
    def objective (self):
        self.obj_func = lpSum(self.allocation*self.value)
        self.model +=  self.obj_func
       
    
    def Constraints(self):
        self.model += lpSum(self.allocation*self.weight) <= self.capacity                 
    def solve(self):
        self.objective()
        self.Constraints()
        self.model.solve()
        self.status =  LpStatus[self.model.status]
        for v in self.model.variables():
            try:
                print(v.name, " = ",v.value())
            except:
                print("error couldnt find value") 
        return self.model.objective.value()

value = [403,	886,	814,	1151,	983,	629,	848,	1074,	839,	819,	1062,	762,	994,	950,	111,	914,	737,	1049,	1152,	1110,	973,	474,	824,	1013,	963,	1101,	1024,	816,	1063,	575,	1153,	447,	1117,	910,	1017,	931,	909,	1126,	1027,	871,	1052,	891,	375,	1131,	318,	705,	1048,	908,	1026,	1061]
weight = [94,	506,	416,	992,	649,	237,	457,	815,	446,	422,	791,	359,	667,	598,	7,	544,	334,	766,	994,	893,	633,	131,	428,	700,	617,	874,	720,	419,	794,	196,	997,	116,	908,	539,	707,	569,	537,	931,	726,	487,	772,	513,	81,	943,	58,	303,	764,	536,	724,	789]
capacity = 997  # max weight of knapsack
number_of_items = 50  # set of items to consider
KNAPSACK=KNAPSACKILP(value,weight,capacity,number_of_items)
print(KNAPSACK.solve())