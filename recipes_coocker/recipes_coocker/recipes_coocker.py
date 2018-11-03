# -*- coding: utf-8 -*-

"""Main module."""

from recipes_scheduling.recipes_scheduling import Recipes
from abc import ABC, abstractmethod

class Cooker(ABC):
    recipe = ''
    def __init__(self):
        print("Coocker instance!")

    def cooks_with(self,recipe):
        self.recipe=recipe
        return self.coocked

    def cooks(self,message):
        #parse message
        return self.coocked

    @abstractmethod
    def with_the(self,recipe):
        pass

    def coocked(self, mex):
        return('coocked '+self.recipe['event'])

class TwoPhaseCommitCooker(Cooker):
    def timeout_in(self, mex):
        return self.recipe['amount']
         
    def timeout_out(self):
        pass
    def not_found(self):
        # http 400
        pass
    def internal_error(self):
        # http 500
        pass
    
    def with_the(self, recipe):
        ## get message type
        ## when message type is equal of the recipe or recipe is all
        self.recipe = recipe
        return self

    def coocks(self, message_type):
        if message_type == self.recipe['messageType'] or 'all'== self.recipe['messageType']:
            return getattr(self, self.recipe['event'])(message_type)
