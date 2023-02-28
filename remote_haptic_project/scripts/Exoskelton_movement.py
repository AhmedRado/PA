#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

zero_joint_msg = Float64()

joint_1_pub = rospy.Publisher("/exoskelaton_plus_hand/joint_1_controller/command", Float64, queue_size=1)
joint_2_pub = rospy.Publisher("/exoskelaton_plus_hand/joint_2_controller/command", Float64, queue_size=1)
joint_3_pub = rospy.Publisher("/exoskelaton_plus_hand/joint_3_controller/command", Float64, queue_size=1)
joint_4_pub = rospy.Publisher("/exoskelaton_plus_hand/joint_4_controller/command", Float64, queue_size=1)
joint_5_pub = rospy.Publisher("/exoskelaton_plus_hand/joint_5_controller/command", Float64, queue_size=1)

def joint_1_callback(joint_1_angle):
    joint_1_pub.publish(joint_1_angle)

def joint_2_callback(joint_2_angle):
    joint_2_pub.publish(joint_2_angle)

def joint_3_callback(joint_3_angle):
    joint_3_pub.publish(joint_3_angle)

def joint_4_callback(joint_4_angle):
    joint_4_pub.publish(joint_4_angle)

def joint_5_callback(joint_5_angle):
    joint_5_pub.publish(joint_5_angle)


def main():
    rospy.init_node("zero_joints")

    joint_1_sub = rospy.Subscriber("/joint_1",Float64,joint_1_callback)
    joint_2_sub = rospy.Subscriber("/joint_2",Float64,joint_2_callback)
    joint_3_sub = rospy.Subscriber("/joint_3",Float64,joint_3_callback)
    joint_4_sub = rospy.Subscriber("/joint_4",Float64,joint_4_callback)
    joint_5_sub = rospy.Subscriber("/joint_5",Float64,joint_5_callback)
    

    rate = rospy.Rate(50.0)
    while not rospy.is_shutdown():
        # joint_5_pub.publish(zero_joint_msg)
        # joint_4_pub.publish(zero_joint_msg)
        # joint_3_pub.publish(zero_joint_msg)
        # joint_2_pub.publish(zero_joint_msg)
        # joint_1_pub.publish(zero_joint_msg)
        rate.sleep()



if __name__ == "__main__":
    main()
