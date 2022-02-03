#!/usr/bin/env python

from operator import eq
import rospy
from touri_mani.msg import TeleopMani

#! Depreciate it in future
#!______________________________________________________
# import stretch_body.robot


# arm_move_step = 0.1
# arm_lift_step = 0.1

# touri = stretch_body.robot.Robot()
# touri.arm.startup()
# touri.lift.startup()

# def update_arm_pos(height, extend):
#     bot_status = touri.get_status()
#     touri_arm_pos = bot_status['arm']['pos'] 
#     touri_lift_pos = bot_status['lift']['pos'] 

#     arm_val = 0
#     lift_val = 0

#     if abs(extend) > 0.75:
#         arm_val = extend
    
#     if abs(height) > 0.75:
#         lift_val = height

#     #TODO: update condition
#     if touri_arm_pos > 0.25 and touri_lift_pos > 0.3:
#         if arm_val > 0:
#             touri.arm.move_by(arm_move_step)
#         if arm_val < 0:
#             touri.arm.move_by(-1*arm_move_step)

#         if lift_val > 0:
#             touri.lift.move_by(arm_lift_step)
#         if arm_val < 0:
#             touri.lift.move_by(arm_lift_step)

#         touri.push_command()


#!______________________________________________________


def callback(data):
    rospy.loginfo("H: {}    E: {}".format(data.height, data.extend))

def listener():
    rospy.init_node('teleop_mani', anonymous=True)
    rospy.Subscriber("teleop_mani", TeleopMani, callback)
    rospy.spin()



if __name__ == "__main__":
    listener()