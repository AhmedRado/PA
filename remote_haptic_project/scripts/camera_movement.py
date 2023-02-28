#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64

zero_joint_msg = Float64()

camera_revolute_z_pub = rospy.Publisher("/ur10e/camera_controller_revolute_z/command", Float64, queue_size=1)
camera_revolute_y_pub = rospy.Publisher("/ur10e/camera_controller_revolute_y/command", Float64, queue_size=1)

def camera_revolute_z_callback(camera_revolute_z_angel):
    camera_revolute_z_pub.publish(camera_revolute_z_angel)

def camera_revolute_y_callback(camera_revolute_y_angel):
    camera_revolute_y_pub.publish(camera_revolute_y_angel)

def main():
    rospy.init_node("zero_joints")

    camera_revolute_z_sub = rospy.Subscriber("/camera_revolute_z",Float64,camera_revolute_z_callback)
    camera_revolute_y_sub = rospy.Subscriber("/camera_revolute_y",Float64,camera_revolute_y_callback)

    rate = rospy.Rate(50.0)
    while not rospy.is_shutdown():

        # camera_revolute_z_pub.publish(zero_joint_msg)
        # camera_revolute_y_pub.publish(zero_joint_msg)

        rate.sleep()



if __name__ == "__main__":
    main()