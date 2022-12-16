#!/usr/bin/env python
import rospy
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from std_msgs.msg import Float64

joint = JointTrajectory()
joint.joint_names = ['shoulder_pan_joint','shoulder_lift_joint','elbow_joint','wrist_1_joint','wrist_2_joint','wrist_3_joint']

point = JointTrajectoryPoint()
point.positions = [2.5,3.5,3,2,1,4]
point.time_from_start = rospy.Duration.from_sec(0.1)

joint.points.append(point)


if __name__ == "__main__":
    rospy.init_node("test")
    pub =rospy.Publisher("/arm_controller/command", JointTrajectory ,queue_size=1)
    rate= rospy.Rate(50)
    while not rospy.is_shutdown():
        pub.publish(joint)
        rate.sleep()