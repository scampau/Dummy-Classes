"""Code to get from practice code into py-households.

These are two example cells written as part of our discussion on July 6th
about how to take classes and functions from dummy code into the live package.

The two different cells are separated by a #%%, the cell marker for Spyder.

Neither of these are necessarily "working", but provide an idea of how to structure
modifications to the package and to Jupyter notebooks.
"""

#%%


#%%
# One way to add functionality is to write a function or class
## that checks every person at every time step to add new classes, functions,
## etc., and then runs the relevant processes as required. 

## This is an example of that: profession is added (along with related functions)
## and then professions are assigned as each person goes through a life course.

jobs = ['blacksmith', 'farmer', 'governor', 'Landlord', 'builder', 'merchant']
jobprobs = (.2,.5,.01,.05,.2,.04)
occupations = {'blacksmith': 50, 'farmer': 20, 'governor': 1000, 'Landlord': 200, 'builder': 50, 'merchant': 250, 'child': 2, 'elderly': 0}

class ProDev():
    
    def __init__(self, adolescence = 14, oldage = 65, jobs = jobs,
                 jobprobs = jobprobs, occupations = occupations):
        self.adolescence = adolescence
        self.oldage = oldage
        self.jobs = jobs
        self.jobprobs = jobprobs
        self.occupations = occupations
    
    def __call__(self, villager):
        #Identify whether this villager has a profession
        if hasattr(villager, 'profession') == False:
            #If they don't, set it up
            villager.profession = None
            def get_profession(self):
                return self.__profession
            
            def set_profession(self, newprofession):
                self.__profession = newprofession
                
            villager.get_profession = get_profession
            villager.set_profession = set_profession

        profession = villager.get_profession(villager)
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
        villager.set_profession(villager.profession)

pd1 = ProDev()

## This then requires that when the simulation runs, pd1 is called on every person
## every year, as follows:
    
while terra.year < 43: #run for 42 years
    terra.progress()
    for p in terra.people:
        pd1(p)


#%%

## Another option is to create a subclass of Person who has these attributes and
## methods added, which then becomes the class of agent for the simulation.
## This will work better shortly following a new update.

class ProDev():
    
    def __init__(self, adolescence = 14, oldage = 65, jobs = jobs,
                 jobprobs = jobprobs, occupations = occupations):
        self.adolescence = adolescence
        self.oldage = oldage
        self.jobs = jobs
        self.jobprobs = jobprobs
        self.occupations = occupations
    
    def __call__(self, villager):
        #Identify whether this villager has a profession
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
    
class Village(Person):
    
    def professions(self):
        if hasattr(self,'profession') == False:
            self.profession = None
            self.__pro_dev = somedefault
            
    def get_profession(self):
        return self.__profession
    
    def set_profession(self, newprofession):
        self.__profession = newprofession
    
    def new_profession(self, pro_dev = None):
        if pro_dev == None:
            pro_dev = self.__pro_dev
        pro_dev(self)