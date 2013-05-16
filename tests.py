import workout_coach

import unittest

class TestObjectCreation(unittest.TestCase):
    def test_default(self):
        coach = workout_coach.Coach()
        assertEqual(len(coach.exercies), 0)
        assertEqual(coach.workout_time, 30)
        assertEqual(coach.rest_time, 10)
