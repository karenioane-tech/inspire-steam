from pysimverse import drone
import cv2
import time

drone= drone()
drone.connect()
time.sleep(1)

drone.take_off(5)
rc_speed=250

if 

while True:
    key=cv2.waitKey(1)& 0xff

#get all values to 0
    left_right=0
    forward_backward=0
    up_down=0
    yaw=0

        left_right, forward_backward, up_down, yaw = new_func(rc_speed, key)
    
    break

drone.send_rc_control(left_right,
                      forward_backward,
                      up_down,
                      yaw)