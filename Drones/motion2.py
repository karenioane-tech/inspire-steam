from pysimverse import Drone
import time
#move drone to target one
drone= Drone(speed=320)  
drone.connect()

drone.take_off(100)
time.sleep(0)

drone.move_left(210)
drone.move_forward(50) #distance in cm


#move drone to target two
drone.take_off(100)
time.sleep(0)
drone.move_forward(108)
drone.move_right(195)


#move drone to target three
drone.take_off(100)
time.sleep(0)
drone.move_forward(120)
drone.move_right(240)
drone.land()







drone.land()