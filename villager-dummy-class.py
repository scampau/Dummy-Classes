# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 10:49:29 2020

@author: scamp
"""

import random as rd
from numpy.random import choice

class Villager(object):
    """A representation of a villager with certain abilities.
    
    Villagers will be initiallized, grow old, get a profession, and collect money.
    
    Parameters:
    -----------
    name: str
        An identifiable unique tag. Used to track individuals.
    age: int
        A measure of how many ticks a villager has experienced plus their 
        initialization.
    profession: str
        A job that the villager does and recieves compensation for.
    money: int
        A measure of how much money the villager has. (currently no other use)
    pay: identity.Pay()
        Calculates how much money a villager earns each tick.
    aging: identity.Aging(years)
        Ages the villager some number of years on each tick.
    pro_dev: ProDev()
        Assigns the villager a profession based on age.
    """
    
    def __init__(self, name, age, profession, money, pay, aging, pro_dev):
        
        self.__name = name
        self.__age = age
        self.__profession = profession
        self.__money = money
        if isinstance(pay, Pay):
            self.__pay = pay
        else:
            return TypeError('pay is notof type Pay')
        if isinstance(aging, Aging):
            self.__aging = aging
        else:
            return TypeError('aging is not of type Aging')
        if isinstance(pro_dev, ProDev):
            self.__pro_dev = pro_dev
        else:
            return TypeError('pro_dev is not of type ProDev')
        
    def get_name(self):
        return self.__name
    
    def set_name(self, new_name):
        self.__name = new_name
    
    def get_age(self):
        return self.__age
    
    def set_age(self, newage):
        self.__age = newage
    
    def new_age(self, aging = None):
        if aging == None:
            aging = self.__aging
        aging(self)
    
    def get_profession(self):
        return self.__profession
    
    def set_profession(self, newprofession):
        self.__profession = newprofession
    
    def new_profession(self, pro_dev = None):
        if pro_dev == None:
            pro_dev = self.__pro_dev
        pro_dev(self)
    
    def get_money(self):
        return self.__money
    
    def set_money(self, income):
        self.__money += income
    
    def new_money(self, pay = None):
        if pay == None:
            pay = self.__pay
        pay(self)

class Pay():
    
    def __init__(self):
        pass

    def __call__(self, villager):
        occupation = villager.get_profession()
        villager.set_money(occupations[occupation])

p_1 = Pay()

class Aging():
    
    def __init__(self, years):
        if type(years) == int:
            if years > 0:
                self.__years = years
            else:
                raise ValueError("years cannot be negative or zero")
        else:
            raise TypeError("years is not an integer")
    
    def __call__(self, villager):
        age = villager.get_age()
        age += self.__years
        villager.set_age(age)

ag_1 = Aging(1)

jobs = ['blacksmith', 'farmer', 'governor', 'Landlord', 'builder', 'merchant']
occupations = {'blacksmith': 50, 'farmer': 20, 'governor': 1000, 'Landlord': 200, 'builder': 50, 'merchant': 250, 'child': 2, 'elderly': 0}

class ProDev():
    
    def __init__(self, adolescence = 14, oldage = 65):
        self.adolescence = adolescence
        self.oldage = oldage
    
    def __call__(self, villager):
        profession = villager.get_profession()
        age = villager.get_age()
        if age <= self.adolescence:
            profession = 'child'
        elif age <= self.oldage:
            if profession is None or 'child':
                if profession not in jobs:
                    profession = choice(jobs, None, p = (.2,.5,.01,.05,.2,.04))
            else:
                pass
        else:
            profession = 'elderly'
        villager.set_profession(profession)

pd_1 = ProDev()

def choose_name():
    name = ''
    for i in range(2):
        x = rd.choice('aeiouy')
        y = rd.choice('bcdfghjklmnpqrstvwxz')
        z = rd.choice('abcdefghijklmnopqrstuvwxyz')
        name = name + x + y + z
    return name

class World(object):
    
    def __init__(self, pop):
        self.community = {}
        self.people = []
        for i in range(pop):
            i_villager = Villager(choose_name(), rd.randint(0,50), None, 0, p_1, ag_1, pd_1)
            self.people.append(i_villager)
            self.community[i_villager.get_name()] = [i_villager.get_age(), i_villager.get_profession(), i_villager.get_money()]
        print(self.community)
    
    def progress(self, years):
        for i in range(years):
            for p in self.people:
                p.new_age()
                p.new_profession()
                p.new_money()
                self.community[p.get_name()] = [p.get_age(), p.get_profession(), p.get_money()]
        print(self.community)