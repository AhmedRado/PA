#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

zero_joint_msg = Float64()

def main():
    rospy.init_node("zero_joints")
    index_joint_1_pub = rospy.Publisher("/hand/index_joint_1_controller/command", Float64, queue_size=1)
    index_joint_2_pub = rospy.Publisher("/hand/index_joint_2_controller/command", Float64, queue_size=1)
    index_joint_3_pub = rospy.Publisher("/hand/index_joint_3_controller/command", Float64, queue_size=1)
    rate = rospy.Rate(50.0)
    while not rospy.is_shutdown():
        index_joint_3_pub.publish(zero_joint_msg)
        index_joint_2_pub.publish(zero_joint_msg)
        index_joint_1_pub.publish(zero_joint_msg)
        rate.sleep()

if __name__ == "__main__":
    main()