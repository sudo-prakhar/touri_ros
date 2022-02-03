#!/usr/bin/env python

import rospy
from touri_nav.msg import TeleopNav

def move_bot_y():
    pass

def turn_bot():
    pass

def callback(data):
    rospy.loginfo("X: {}    Y: {}".format(data.x, data.y))

def listener():
    rospy.init_node('teleop_nav', anonymous=True)
    rospy.Subscriber("teleop_nav", TeleopNav, callback)
    rospy.spin()



if __name__ == "__main__":
    listener()