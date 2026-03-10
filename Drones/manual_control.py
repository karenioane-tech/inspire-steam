from pysimverse import Drone
import time
import keyboard
import cv2 

drone = Drone()

drone.take_off() # Distance is in cm
time.sleep(2)

drone.take_off(5) # Distance is in cm
rc_speed = 250

while True:
    key = keyboard.read_key()

#get all values 0
    left_right = 0
    foward_back = 0
    up_down = 0
    yaw = 0

    if key == 'w':
        foward_back = rc_speed
    elif key == 's':
        foward_back = -rc_speed
    elif key == 'a':
        left_right = -rc_speed  
    elif key == 'd':
        left_right = rc_speed
    elif key == 'q':
        yaw = -1
    elif key == 'e':
        yaw = 1
    elif key == 'r':
        up_down = rc_speed
    elif key == 'f':
        up_down = -rc_speed
        break
    drone.send_rc_control(left_right, foward_back, up_down, yaw)