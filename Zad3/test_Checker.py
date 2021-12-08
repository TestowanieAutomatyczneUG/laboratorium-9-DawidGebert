import unittest
from datetime import datetime
from unittest.mock import Mock
from Checker import Checker

class test_Checker(unittest.TestCase):

    def setUp(self):
        self.temp = Checker()

    def test_checker_after_17(self):
        self.temp.env.getTime = Mock(name = 'getTime')
        self.temp.env.getTime.return_value = datetime(2021, 12, 1, 22, 15, 10, 222222)
        self.temp.resetWav()
        self.temp.remainder()
        self.assertTrue(self.temp.returnWav())
    
    def test_checker_before_17(self):
        self.temp.env.getTime = Mock(name = 'getTime')
        self.temp.env.getTime.return_value = datetime(2021, 12, 1, 14, 30, 10, 222222)
        self.temp.resetWav()
        self.temp.remainder()
        self.assertFalse(self.temp.returnWav())

