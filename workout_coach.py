#!/usr/bin/env python

import subprocess, time


class Coach(object):
    def __init__(self, exercises=[], workout_time=30, rest_time=10):
        self.exercises = exercises
        self.workout_time = workout_time
        self.rest_time = rest_time

    def run_workout(self):

        for exercise in self.exercises:
            time.sleep(1)
            subprocess.call(["say", exercise])
            time.sleep(self.workout_time)
            #TODO think of better way to skip the last exercise
            if (exercise != "side plank"):
                subprocess.call(["say", "rest"])
                time.sleep(self.rest_time - 1)

        subprocess.call(["say", "Done"])
    


if __name__ == '__main__':
    coach = Coach(exercises=["jumping jacks",
                             "wall sit",
                             "push up",
                             "crunch",
                             "step up on chair",
                             "squat",
                             "triceps dip",
                             "plank",
                             "high knees",
                             "lunge",
                             "push up and rotate",
                             "side plank"])
    coach.run_workout()






