# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 18:31:11 2020

@author: scamp
"""


import random

""" Random generator for true or false with a parameter for probability"""
def rate(skew):
    
    prob = random.random()
    if prob >= skew:
        return True
    if prob < skew:
        return False

""" My person class with a name and an age. Has getters and setters"""
class person(object):
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_name(self, newname = None):
        self.name = newname
    
    def set_age(self, newage = None):
        self.age = newage

""" My function class that will increase the age of a person by one year"""
class aging():
    
    def __init__(self, person):
        self.age = person.get_age()
        self.age += 1
        return self.age

""" My world object in which the simulation will run. creates a population of
    people with an age and name. will eventually run the aging function within
"""
class world(object):
    
    def __init__(self, pop):
        community = {}
        for i in range(pop):
            i_person = person(i, random.randint(0,50))
            if i_person not in community:
                community[i] = i_person.get_age()
        print (community)


world_1 = world(10)


sam = person('Sam', 24)
aging(sam)
print (sam.get_age())
# print(0.get_age())