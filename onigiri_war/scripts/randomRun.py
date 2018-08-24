#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
import random

from geometry_msgs.msg import Twist
#from std_msgs.msg import String
#from sensor_msgs.msg import Image
#from cv_bridge import CvBridge, CvBridgeError
#import cv2



class RandomBot():
    def __init__(self, bot_name):
        # bot name 
        self.name = bot_name
        # velocity publisher
        self.vel_pub = rospy.Publisher('cmd_vel', Twist,queue_size=1)

    def strategy(self):

        i = 0

        r = rospy.Rate(10) # change speed 1fps

        target_speed = 0
        target_turn = 0
        control_speed = 0
        control_turn = 0

        PI = 3.14159265358979
        
        while not rospy.is_shutdown():

            # twist = self.calcTwist()
            twist = Twist()
            # twist.linear.x = 0
            # twist.angular.z= 0


            if 10 <= i and i < 40:
                twist.linear.x = 0.4
                twist.angular.z = 0
            elif 50 <= i and i < 60:
                twist.linear.x = 0
                twist.angular.z = PI/4
            elif 70 <= i and i < 95:
                twist.angular.z = 0  
                twist.linear.x = 0.47
            elif 105 <= i and i < 125:
                twist.linear.x = 0
                twist.angular.z = -(PI/4) 
            elif 135 <= i and i < 147:
                twist.linear.x = 1.0
                twist.angular.z = 0 
            elif 185 <= i and i < 213:
                twist.linear.x = 1.0
                twist.angular.z = 0 
            elif 220 <= i and i < 230:
                twist.linear.x = 0
                twist.angular.z = (PI/2) 
            elif 240 <= i and i < 255:
                twist.linear.x = 1
                twist.angular.z = 0
            elif 265 <= i and i < 275:
                twist.linear.x = 0
                twist.angular.z = (PI*3/4) 
            elif 280 <= i and i < 283:
                twist.linear.x = 1
                twist.angular.z = 0

            else:
                twist.linear.x = 0
                twist.angular.z = 0

            print(twist)
            self.vel_pub.publish(twist)

            i = i + 1

            r.sleep()
 

if __name__ == '__main__':
    rospy.init_node('random_rulo')
    bot = RandomBot('Random')
    bot.strategy()

