from pysimverse import Drone
import time

drone= Drone(speed=300)  
drone.connect()

drone.take_off(100)

drone.move_forward(250)
drone.move_left(100)
drone.move_right(350)

drone.land()