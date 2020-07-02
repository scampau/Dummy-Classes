# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 18:31:11 2020

@author: scamp
"""


import random
#not needed necessarily, just for a demo
import sys
sys.path.append('C:\\github\\house-inheritance\\code')
import households

# DC: docstrings should go inside the function to have them pop up in tooltips.

# DC: right now skew determines the probability that an event will be false - 
## many people think primarily in terms of probability an event will happen, 
## rather than that it won't, so you may wish to switch around your equalities.
def rate(skew):
    """Random generator for true or false with a parameter for probability.
    
    Uses the random.random number generator to decide if an event happens.
    
    Parameters
    ----------
    skew
        The probability that an event doesn't happen
    
    Returns
    -------
    bool
        Did the event happen?
    """
    prob = random.random()
    if prob >= skew:
        return True
    if prob < skew:
        return False


# DC: classes are conventionally capitalized; 
class Person(object):
    """ My person class with a name and an age. Has getters and setters.
    
    Parameters
    ----------
    name : str
    age : int
    """
    def __init__(self, name, age, aging):
        self.__name = name
        self.__age = age
        if isinstance(aging, Aging):
            self.__aging = aging
        else:
            raise TypeError("aging isn't of type Aging")
        
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def set_name(self, newname = None):
        self.__name = newname
    
    def set_age(self, newage = None):
        self.__age = newage
        
    def new_age(self,aging = None):
        if aging == None:
            aging = self.__aging
        aging(self)

class Aging():
    """ My function class that will increase the age of a person by some number of years
    
    Parameters
    ----------
    years : int
        The number of years a person will be aged
    
    
    """
    def __init__(self, years):
        if type(years) == int:
            if years > 0:
                self.__years = years
            else:
                raise ValueError("years cannot be negative or zero")
        else:
            raise TypeError("years is not an integer")
    
    def __call__(self,person):
        """Age a person a certain number of years."""
        age = person.get_age() #get the age of a person
        age += self.__years #add the right number of yeras
        person.set_age(age)
        
        


class World(object):
    """ My world object in which the simulation will run. creates a population of
    people with an age and name. will eventually run the aging function within
    """
    def __init__(self, pop):
        self.community = {} #the on
        self.people = []
        for i in range(pop):
            i_person = Person(i, random.randint(0,50))
            self.people.append(i_person)
            self.community[i_person.get_name()] = i_person.get_age()
        print(self.community)
        
    def get_names(self):
        """Output a list of names for the people"""
        names = []
        for p in self.people:
            names.append(p.get_name())
        return names
    
    def get_names_short(self):
        """List comprehension version of get_names"""
        return [p.get_name() for p in self.people]







#The actual code

# world_1 = world(10)


# sam = person('Sam', 24)
# aging(sam)
# print (sam.get_age())
# # print(0.get_age())