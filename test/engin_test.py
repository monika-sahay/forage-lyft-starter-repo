from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willough_engine import WilloughbyEngine

import unittest
import datetime

class TestCapuletEngine(unittest.TestCase):
    def test_need_service_true(self):
        current_mileage = 30001
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage,last_service_mileage)
        self.assertTrue(engine.needs_service())


    def test_need_service_false(self):
        current_mileage = 3000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage,last_service_mileage)
        self.assertFalse(engine.needs_service())


class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service_true(self):
        current_mileage = 67031
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        current_mileage = 60019
        last_service_mileage = 20
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())



class TestSternmanEngine(unittest.TestCase):
    def test_needs_service_true(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_need_servce_false(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())
