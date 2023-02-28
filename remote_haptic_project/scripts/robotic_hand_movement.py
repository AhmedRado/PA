#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

zero_joint_msg = Float64()

ring_joint_1_pub = rospy.Publisher("/exoskelaton_plus_hand/ring_joint_1_controller/command", Float64, queue_size=1)
ring_joint_2_pub = rospy.Publisher("/exoskelaton_plus_hand/ring_joint_2_controller/command", Float64, queue_size=1)
ring_joint_3_pub = rospy.Publisher("/exoskelaton_plus_hand/ring_joint_3_controller/command", Float64, queue_size=1)
index_joint_1_pub = rospy.Publisher("/exoskelaton_plus_hand/index_joint_1_controller/command", Float64, queue_size=1)
index_joint_2_pub = rospy.Publisher("/exoskelaton_plus_hand/index_joint_2_controller/command", Float64, queue_size=1)
index_joint_3_pub = rospy.Publisher("/exoskelaton_plus_hand/index_joint_3_controller/command", Float64, queue_size=1)
middle_joint_1_pub = rospy.Publisher("/exoskelaton_plus_hand/middle_joint_1_controller/command", Float64, queue_size=1)
middle_joint_2_pub = rospy.Publisher("/exoskelaton_plus_hand/middle_joint_2_controller/command", Float64, queue_size=1)
middle_joint_3_pub = rospy.Publisher("/exoskelaton_plus_hand/middle_joint_3_controller/command", Float64, queue_size=1)
thumb_joint_1_pub = rospy.Publisher("/exoskelaton_plus_hand/thumb_joint_1_controller/command", Float64, queue_size=1)
thumb_joint_2_pub = rospy.Publisher("/exoskelaton_plus_hand/thumb_joint_2_controller/command", Float64, queue_size=1)
thumb_joint_3_pub = rospy.Publisher("/exoskelaton_plus_hand/thumb_joint_3_controller/command", Float64, queue_size=1)
little_joint_1_pub = rospy.Publisher("/exoskelaton_plus_hand/little_joint_1_controller/command", Float64, queue_size=1)
little_joint_2_pub = rospy.Publisher("/exoskelaton_plus_hand/little_joint_2_controller/command", Float64, queue_size=1)
little_joint_3_pub = rospy.Publisher("/exoskelaton_plus_hand/little_joint_3_controller/command", Float64, queue_size=1)

link_5_to_palm_pub = rospy.Publisher("/exoskelaton_plus_hand/link_5_to_palm_controller/command", Float64, queue_size=1)

def ring_joint_1_callback(ring_joint_1_angel):
    ring_joint_1_pub.publish(ring_joint_1_angel)

def ring_joint_2_callback(ring_joint_2_angel):
    ring_joint_2_pub.publish(ring_joint_2_angel)

def ring_joint_3_callback(ring_joint_3_angel):
    ring_joint_3_pub.publish(ring_joint_3_angel)

def index_joint_1_callback(index_joint_1_angel):
    index_joint_1_pub.publish(index_joint_1_angel)

def index_joint_2_callback(index_joint_2_angel):
    index_joint_2_pub.publish(index_joint_2_angel)

def index_joint_3_callback(index_joint_3_angel):
    index_joint_3_pub.publish(index_joint_3_angel)

def middle_joint_1_callback(middle_joint_1_angel):
    middle_joint_1_pub.publish(middle_joint_1_angel)

def middle_joint_2_callback(middle_joint_2_angel):
    middle_joint_2_pub.publish(middle_joint_2_angel)

def middle_joint_3_callback(middle_joint_3_angel):
    middle_joint_3_pub.publish(middle_joint_3_angel)

def thumb_joint_1_callback(thumb_joint_1_angel):
    thumb_joint_1_pub.publish(thumb_joint_1_angel)

def thumb_joint_2_callback(thumb_joint_2_angel):
    thumb_joint_2_pub.publish(thumb_joint_2_angel)

def thumb_joint_3_callback(thumb_joint_3_angel):
    thumb_joint_3_pub.publish(thumb_joint_3_angel)

def little_joint_1_callback(little_joint_1_angel):
    little_joint_1_pub.publish(little_joint_1_angel)

def little_joint_2_callback(little_joint_2_angel):
    little_joint_2_pub.publish(little_joint_2_angel)

def little_joint_3_callback(little_joint_3_angel):
    little_joint_3_pub.publish(little_joint_3_angel)

def link_5_to_palm_callback(link_5_to_palm_angel):
    link_5_to_palm_pub.publish(link_5_to_palm_angel)

def main():
    rospy.init_node("zero_joints")

    ring_joint_1_sub = rospy.Subscriber("/ring_joint_1", Float64, ring_joint_1_callback)
    ring_joint_2_sub = rospy.Subscriber("/ring_joint_2", Float64, ring_joint_2_callback)
    ring_joint_3_sub = rospy.Subscriber("/ring_joint_3", Float64, ring_joint_3_callback)
    index_joint_1_sub = rospy.Subscriber("/index_joint_1", Float64, index_joint_1_callback)
    index_joint_2_sub = rospy.Subscriber("/index_joint_2", Float64, index_joint_2_callback)
    index_joint_3_sub = rospy.Subscriber("/index_joint_3", Float64, index_joint_3_callback)
    middle_joint_1_sub = rospy.Subscriber("/middle_joint_1", Float64, middle_joint_1_callback)
    middle_joint_2_sub = rospy.Subscriber("/middle_joint_2", Float64, middle_joint_2_callback)
    middle_joint_3_sub = rospy.Subscriber("/middle_joint_3", Float64, middle_joint_3_callback)
    thumb_joint_1_sub = rospy.Subscriber("/thumb_joint_1", Float64, thumb_joint_1_callback)
    thumb_joint_2_sub = rospy.Subscriber("/thumb_joint_2", Float64, thumb_joint_2_callback)
    thumb_joint_3_sub = rospy.Subscriber("/thumb_joint_3", Float64, thumb_joint_3_callback)
    little_joint_1_sub = rospy.Subscriber("/little_joint_1", Float64, little_joint_1_callback)
    little_joint_2_sub = rospy.Subscriber("/little_joint_2", Float64, little_joint_2_callback)
    little_joint_3_sub = rospy.Subscriber("/little_joint_3", Float64, little_joint_3_callback)

    link_5_to_palm_sub = rospy.Subscriber("link_5_to_palm", Float64, link_5_to_palm_callback)

    rate = rospy.Rate(50.0)
    while not rospy.is_shutdown():
        # ring_joint_1_pub.publish(zero_joint_msg)
        # ring_joint_2_pub.publish(zero_joint_msg)
        # ring_joint_3_pub.publish(zero_joint_msg)
        # index_joint_3_pub.publish(zero_joint_msg)
        # index_joint_2_pub.publish(zero_joint_msg)
        # index_joint_1_pub.publish(zero_joint_msg)
        # middle_joint_1_pub.publish(zero_joint_msg)
        # middle_joint_2_pub.publish(zero_joint_msg)
        # middle_joint_3_pub.publish(zero_joint_msg)
        # thumb_joint_1_pub.publish(zero_joint_msg)
        # thumb_joint_2_pub.publish(zero_joint_msg)
        # thumb_joint_3_pub.publish(zero_joint_msg)
        # little_joint_1_pub.publish(zero_joint_msg)
        # little_joint_2_pub.publish(zero_joint_msg)
        # little_joint_3_pub.publish(zero_joint_msg)
        rate.sleep()

if __name__ == "__main__":
    main()
