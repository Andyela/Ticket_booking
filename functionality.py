import unittest

from data import Event


class EventTests (unittest.TestCase):
    def test_for_object_instance(self):
        event = Event(1, 'birthday', 11 - 11 - 2016, 18 - 11 - 2016)
        self.assertIsInstance(event, Event, msg = "Check class Instance")
