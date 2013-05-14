#!/usr/bin/env python

import subprocess, time

exercises = ["jumping jacks",
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
              "side plank"]

for exercise in exercises:
    time.sleep(1)
    subprocess.call(["say", exercise])
    time.sleep(30)
    if (exercise != "side plank"):
        subprocess.call(["say", "rest"])
        time.sleep(9)

subprocess.call(["say", "Done"])
