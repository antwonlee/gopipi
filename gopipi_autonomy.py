from gopigo import *
import time
import random

min_distance = 70

def autonomy():
    no_problem = True
    while no_problem:
        servo(70)
        time.sleep(1)
        dist = us_dist(15)
        if dist > min_distance:
            print('Forward is fine with me', dist)
            fwd()
            time.sleep(1)
        else:
            print('Stuff is in the way', dist)
            stop()
            servo(28)
            time.sleep(1)
            left_dir = us_dist(15)
            time.sleep(1)
            servo(112)
            right_dir = us_dist(15)
