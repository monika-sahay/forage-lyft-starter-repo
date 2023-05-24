import unittest

from tires.tires_type.carrigan_tires import CarriganTires
from tires.tires_type.octoprime_tires import OctoprimeTires


class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.7,0.8, 1, 0.9]
        tire = CarriganTires(tire_wear)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0.7,0.8, 0.6, 0.4]
        tire = CarriganTires(tire_wear)
        self.assertFalse(tire.needs_service())

class TestOctoPrimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [1,1, 1, 0.9]
        tire = OctoprimeTires(tire_wear)
        self.assertFalse(tire.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0.5, 0.6, 0.4, 0.7]
        tire = OctoprimeTires(tire_wear)
        self.assertFalse(tire.needs_service())