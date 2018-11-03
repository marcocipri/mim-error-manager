# -*- coding: utf-8 -*-

"""Main module."""

import yaml


class Recipes(object):
    tests = ''

    def __init__(self, testsFile):
        with open(testsFile, 'r') as ymlfile:
            self.tests = yaml.load(ymlfile)

    def getKey(self, time, key):
        print("get %s %s" % (time, key))
        try:
            val = self.tests['tests'][time][key]
        except KeyError as identifier:
            val = 0
        return val


class ScheduledRecipes(Recipes):

    def __init__(self, testsFile):
        super().__init__(testsFile)

    def scheduledAt(self, time):
        recipe = {'event': 'null'}
        contLength = 0
        while(recipe == {'event': 'null'} and contLength < 3):
            recipe = self.getScheduled(
                time[:len(time)-contLength] +
                '*'*contLength)
            contLength = contLength + 1
        # print(recipe)
        return recipe

    def getScheduledRecipeKey(self, time, key):
        val = 0
        event = self.scheduledAt(time)
        try:
            val = event[key]
        except KeyError as identifier:
            val = None
        return val

    def getScheduled(self, time):
        print("get %s " % (time))
        try:
            recipe = self.tests['tests'][time]
        except KeyError as identifier:
            recipe = {'event': 'null'}
        return recipe
