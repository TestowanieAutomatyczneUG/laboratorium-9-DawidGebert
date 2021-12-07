import unittest
from CarImpl import CarImpl
from Car import Car
from unittest.mock import Mock


class test_CarImpl(unittest.TestCase):
    def setUp(self):
        self.temp = Car()
    
    def test_needsFuel_true(self):
        self.temp.needsFuel = Mock(name = 'needsFuel')
        self.temp.needsFuel.return_value = True
        carimpl=CarImpl(self.temp)
        self.assertEqual(carimpl.impl_checkFuel(),"Wystarczająco Paliwa")

    def test_needsFuel_false(self):
        self.temp.needsFuel = Mock(name = 'needsFuel')
        self.temp.needsFuel.return_value = False
        carimpl = CarImpl(self.temp)
        self.assertEqual(carimpl.impl_checkFuel(),"Za Mało paliwa")

    def test_getEngineTemperature_70(self):
        self.temp.getEngineTemperature = Mock(name = 'getEngineTemperature')
        self.temp.getEngineTemperature.return_value = 70
        carimpl = CarImpl(self.temp)
        self.assertEqual(carimpl.impl_checkEngineTemperature(),"Normalna temperatura silnika")

    def test_getEngineTemperature_150(self):
        self.temp.getEngineTemperature = Mock(name = 'getEngineTemperature')
        self.temp.getEngineTemperature.return_value = 150
        carimpl = CarImpl(self.temp)
        self.assertEqual(carimpl.impl_checkEngineTemperature(),"Silnik za gorący")

    def test_driveTo_Gdansk(self):
        self.temp.driveTo=Mock(name = 'driveTo')
        self.temp.driveTo.return_value='Gdańsk'
        carimpl = CarImpl(self.temp)
        self.assertEqual(carimpl.impl_setDesitnation('Gdańsk'),"Kierunek to Gdańsk")

    def test_driveTo_Berlin(self):
        self.temp.driveTo=Mock(name = 'driveTo')
        self.temp.driveTo.return_value='Berlin'
        carimpl = CarImpl(self.temp)
        self.assertEqual(carimpl.impl_setDesitnation('Berlin'),"Kierunek to Berlin")