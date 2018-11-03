#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `testscheduling` package."""


import unittest
import os

from recipes_scheduling import Recipes
from recipes_scheduling import ScheduledRecipes


class TestTestscheduling(unittest.TestCase):
    """Tests for `testscheduling` package."""
    dirPath =''
    confFile= ''
    def setUp(self):
        """Set up test fixtures, if any."""
        self.dirPath = os.path.dirname(os.path.realpath(__file__))
        self.confFile = self.dirPath+"/confAamsTestProxy.yml"
    def tearDown(self):
        """Tear down test fixtures, if any."""



    def test_noEvent(self):
        self.assertEqual(
            ScheduledRecipes(self.confFile).scheduledAt('10-10'), {'event': 'null'} )

    def test_foundedEventùEsactTime1(self):
        self.assertEqual(
            ScheduledRecipes(self.confFile).scheduledAt('16-54'), 
            {'amount': 10001, 'event': 'timeout', 'message': 'all', 'operator': 'all'} 
            )

    def test_foundedEventEsactTime2(self):
        self.assertEqual(
            ScheduledRecipes(self.confFile).scheduledAt('18-08'), 
            {'amount': 10002, 'event': 'timeout1', 'message': 200, 'operator': 15028} 
            )

    def test_foundedEventRangeOfTime1(self):
        self.assertEqual(
            ScheduledRecipes(self.confFile).scheduledAt('18-07'), 
            {'event': 'timeout2', 'message': 200, 'operator': 15028, 'timeout': 10003}
            )

    def test_foundedEventRangeOfTime2(self):
        self.assertEqual(
            ScheduledRecipes(self.confFile).scheduledAt('18-17'), 
            {'event': 'timeout2', 'message': 200, 'operator': 15028, 'timeout': 10002}
            )

    def test_foundedEventKey1(self):
        self.assertEqual(
            ScheduledRecipes(self.confFile).getScheduledRecipeKey('10-10','test'), 
            None
            )

    def test_foundedEventKey2(self):
        self.assertEqual(
            ScheduledRecipes(self.confFile).getScheduledRecipeKey('16-54','test'), 
            None
            )


    def test_foundedEventKey3(self):
        self.assertEqual(
            ScheduledRecipes(self.confFile).getScheduledRecipeKey('16-54','timeout'), 
            None
            )

    def test_foundedEventKey4(self):
        self.assertEqual(
            ScheduledRecipes(self.confFile).getScheduledRecipeKey('16-54','amount'), 
            10001
            )

    def test_foundedEventKey5(self):
        self.assertEqual(
            ScheduledRecipes(self.confFile).getScheduledRecipeKey('11-10','amount'), 
            '10001'
            )

if __name__ == '__main__':
    unittest.main()

# playRules(schedule.at(time).forOperator().forMessage())