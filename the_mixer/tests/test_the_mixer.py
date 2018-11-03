#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `the_mixer` package."""


import unittest
import pytest
import os
from the_mixer import the_mixer
from recipes_scheduling import ScheduledRecipes
from recipes_coocker.recipes_coocker import TwoPhaseCommitCooker


class TestThe_mixer(unittest.TestCase):
    """Tests for `the_mixer` package."""

    dirPath = ''
    confFile = ''

    def setUp(self):
        """Set up test fixtures, if any."""
        self.dirPath = os.path.dirname(os.path.realpath(__file__))
        self.confFile = self.dirPath+"/confAamsTestProxy.yml"

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_noEvent(self):
        self.assertEqual(
            ScheduledRecipes(self.confFile).scheduledAt('10-10'),
            {'event': 'null'})

    def test_foundedEventEsactTime1(self):
        self.assertEqual(
            ScheduledRecipes(self.confFile).scheduledAt('16-54'),
            {'amount': 10001, 'event': 'timeout_in',
                'messageType': 'all', 'operator': 'all'}
            )

    def test_foundedEventEsactTime2(self):
        self.assertEqual(
            ScheduledRecipes(self.confFile).scheduledAt('18-08'),
            {'amount': 10002, 'event': 'timeout_in',
                'messageType': 200, 'operator': 15028}
            )

    def test_foundedEventRangeOfTime1(self):
        self.assertEqual(
            ScheduledRecipes(self.confFile).scheduledAt('18-07'),
            {'event': 'timeout_in', 'messageType': 200,
                'operator': 15028, 'timeout': 10003}
            )

    def test_foundedEventRangeOfTime2(self):
        self.assertEqual(
            ScheduledRecipes(self.confFile).scheduledAt('18-17'),
            {'event': 'timeout_in', 'messageType': 200,
                'operator': 15028, 'timeout': 10002}
            )

    def test_foundedEventKey1(self):
        self.assertEqual(
            ScheduledRecipes(self.confFile).getScheduledRecipeKey(
                '10-10', 'test'), None)

    def test_foundedEventKey2(self):
        self.assertEqual(
            ScheduledRecipes(self.confFile).
            getScheduledRecipeKey('16-54', 'test'),
            None
            )

    def test_foundedEventKey3(self):
        self.assertEqual(
            ScheduledRecipes(self.confFile).getScheduledRecipeKey(
                '16-54', 'timeout'),
            None
            )

    def test_foundedEventKey4(self):
        self.assertEqual(
            ScheduledRecipes(self.confFile).getScheduledRecipeKey(
                '16-54', 'amount'),
            10001
            )

    def test_foundedEventKey5(self):
        self.assertEqual(
            ScheduledRecipes(self.confFile).getScheduledRecipeKey(
                '11-10', 'amount'),
            '10001'
            )

    def test_mytest1(self):
        theCoocker = TwoPhaseCommitCooker()
        recipe = ScheduledRecipes(self.confFile).scheduledAt('11-11')
        print(recipe['event'])
        self.assertEqual(theCoocker.with_the(
            recipe).coocks('ciccio'), '10001')

    def test_mytest2(self):
        theCoocker = TwoPhaseCommitCooker()
        recipe = ScheduledRecipes(self.confFile).scheduledAt('11-12')
        print(recipe['event'])
        self.assertEqual(theCoocker.with_the(
            recipe).coocks('prepare'), '10001')

# SpecificProtocol inherit GenericCoockingProtocol
# coocker.playsWith(SpecificProtocol)
# thePbadCoocker.coocks_with(scheduled_at(11-20))(message)
# thePbadCoocker.coocks(message).with_the(recipes.scheduledAt(11-20))
