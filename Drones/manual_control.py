from pysimverse import Drone
import time
import cv2 
import cvzone
drone = Drone()

drone.take_off() # Distance is in cm
time.sleep(2)

drone.take_off(5) # Distance is in cm
rc_speed = 250

while True:
    key = cv2.waitKey(1) & 0xFF

#get all values 0
    left_right = 0
    foward_back = 0
    up_down = 0
    yaw = 0

    if key == ord('w'):
        foward_back = rc_speed
    elif key == ord('s'):
        foward_back = -rc_speed
    elif key == ord('a'):
        left_right = -rc_speed  
    elif key == ord('d'):
        left_right = rc_speed
    elif key == ord('q'):
        yaw = -1
    elif key == ord('e'):
        yaw = 1
    elif key == ord('r'):
        up_down = rc_speed
    elif key == ord('f'):
        up_down = -rc_speed
        break
    drone.send_rc_control(left_right, foward_back, up_down, yaw)